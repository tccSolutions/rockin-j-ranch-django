import os
import random
from django.shortcuts import redirect, render
from .models import Horse, Image
from .forms import ImageForm
import cloudinary
import cloudinary.uploader
from django.views.decorators.clickjacking import xframe_options_exempt
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from datetime import date
cloudinary.config( 
  cloud_name = os.getenv("CLOUDINARY_NAME"), 
  api_key = os.getenv("CLOUDINARY_API_KEY"), 
  api_secret = os.getenv("CLOUDINARY_API_SECRET")
)

@xframe_options_exempt
def horse(request, name, pk):   
    selected_horse = Horse.objects.get(id=pk)
    images = Image.objects.filter(horse=selected_horse)   
    if len(images) > 0:
        profile_image = random.choice(images)
    else:
        profile_image = ""
    image_form = ImageForm()
    if selected_horse.girth and selected_horse.length:
        selected_horse.weight = round(((selected_horse.girth**2 ) * selected_horse.length)/300)
    selected_horse.age = date.today().year - selected_horse.year_foaled    
    context = {'horse': selected_horse, 'images':images, 'image_form':image_form, 'profile_image': profile_image}
    return render(request, 'horse/horse.html', context)

def add_image(request, pk):
    if request.method == "POST":       
        image = cloudinary.uploader.upload(request.FILES['image'])
        current_horse = Horse.objects.get(id=request.POST['horse'])
        new_image = Image(comment=request.POST['comment'],horse=current_horse, url=image["url"], name=image['public_id'])        
        new_image.save()
    return redirect(horse, pk=current_horse.id)

def delete_image(request):
    if request.method == "POST":  
        current_horse = Horse.objects.get(id=request.POST['horse'])
        image = Image.objects.get(name=request.POST['name']) 
        cloudinary.uploader.destroy(public_id=image.name)
        image.delete()
    return redirect(horse, pk=current_horse.id)

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
    

