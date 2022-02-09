import os
import random
from django.http import JsonResponse
from django.shortcuts import redirect, render
from .models import Horse, Image, Note, Medical
import cloudinary
import cloudinary.uploader
from django.views.decorators.clickjacking import xframe_options_exempt
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from datetime import date, datetime

cloudinary.config( 
  cloud_name = os.getenv("CLOUDINARY_NAME"), 
  api_key = os.getenv("CLOUDINARY_API_KEY"), 
  api_secret = os.getenv("CLOUDINARY_API_SECRET")
)

#View homepage from iframe
@xframe_options_exempt
#horse load page
def horse(request, name, pk):   
    selected_horse = Horse.objects.get(id=pk)
    images = Image.objects.filter(horse=selected_horse)   
    if len(images) > 0:
        profile_image = random.choice(images)
        while profile_image.private_image:
            profile_image = random.choice(images)
    else:
        profile_image = ""    
    if selected_horse.girth and selected_horse.length:
        selected_horse.weight = round(((selected_horse.girth**2 ) * selected_horse.length)/300)
    elif Medical.objects.filter(horse=selected_horse):
        new_weight = 0
        weight_date=0
        for record in Medical.objects.filter(horse=selected_horse):            
            if record.weight:
               new_weight = record.weight
               weight_date = record.date
               if weight_date >= record.date:
                   selected_horse.weight = new_weight
    selected_horse.age = date.today().year - selected_horse.year_foaled    
    context = {'horse': selected_horse, 'images':images, 'profile_image': profile_image}
    return render(request, 'horse/horse.html', context)

#add image
def add_image(request):   
    if request.method == "POST":  
        try:          
            current_horse = Horse.objects.get(id=request.POST['horse'])                       
            image = cloudinary.uploader.upload(request.FILES['image'], public_id=f"rockin-j-ranch/{current_horse.name}/{id(request.FILES['image'])}")         
            new_image = Image(comment=request.POST['comment'],horse=current_horse, url=image["url"], name=id(request.FILES['image']))        
            new_image.save()
        except Exception as e:
          print(e)
          messages.warning(request, e)
    return redirect(horse, name=current_horse.name, pk=current_horse.id)

#delete image
def delete_image(request):
    if request.method == "POST":  
        current_horse = Horse.objects.get(id=request.POST['horse'])
        image = Image.objects.get(name=request.POST['name']) 
        cloudinary.uploader.destroy(public_id=image.name)
        image.delete()
    return redirect(horse, name=current_horse.name, pk=current_horse.id)

#notes page
def notes(request, pk):   
    horse = Horse.objects.get(id=pk)
    if Image.objects.filter(horse=horse):
        horse.image = Image.objects.filter(horse=horse).first()
        print(horse.image)    
    training_notes = Note.objects.filter(horse=horse.id)  
    context={'horse':horse, 'training_notes': training_notes, }

    #add note
    if request.method == "POST":
        try:
            note = Note.objects.get(date=request.POST['date'], horse=horse)
            note.note = request.POST['note']
            note.save()
            return redirect(notes, pk=horse.id)
        except:
            new_note = Note(date=request.POST['date'], note=request.POST['note'], horse=horse)
            new_note.save()
            messages.info(request, "Note Successfully Saved")
            return redirect(notes, pk=horse.id)
    return render(request, "horse/training_notes.html", context)

#Get Horse Medical Data
def get_medical(request, pk):
    horse = Horse.objects.get(id=pk)  
    medical_records = Medical.objects.filter(horse=horse).values()     
    return JsonResponse(list(medical_records), safe=False)

#Request info on Horse
def request_info(request):
    if request.method == "POST":        
        subject = request.POST['horse_name']
        message = f"Name: {request.POST['name']}\nEMAIL: {request.POST['email']}\n\n{request.POST['message']}"
        if not request.POST['name']:
            messages.error(request, "Please enter your name")
        elif not request.POST['email']:
            messages.error(request, "Please enter your email")
        elif not request.POST['message']:
            messages.error(request, "Please ask a question")
        else:
            try:
                send_mail(
                    subject,
                    message,
                    settings.EMAIL_HOST_USER,
                    ['rockingjranch369@yahoo.com', 'dmobley0608@gmail.com'],
                    fail_silently=False
                )
                messages.info(request, "Thank you! Your message has been sent.")
            except:
                messages.error(request, 'Error Sending Message')
    return redirect(request.META['HTTP_REFERER'])
    

