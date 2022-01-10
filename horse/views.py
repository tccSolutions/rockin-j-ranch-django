import os
import random
from django.shortcuts import redirect, render
from .models import Horse, Image
from .forms import ImageForm
import cloudinary
import cloudinary.uploader
from django.views.decorators.clickjacking import xframe_options_exempt



cloudinary.config( 
  cloud_name = os.getenv("CLOUDINARY_NAME"), 
  api_key = os.getenv("CLOUDINARY_API_KEY"), 
  api_secret = os.getenv("CLOUDINARY_API_SECRET")
)

@xframe_options_exempt
def horse(request, pk):    
    selected_horse = Horse.objects.get(id=pk)
    images = Image.objects.filter(horse=selected_horse)   
    if len(images) > 0:
        profile_image = random.choice(images)
    else:
        profile_image = ""
    image_form = ImageForm()
    selected_horse.weight = round(((selected_horse.girth**2 ) * selected_horse.length)/300)
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
