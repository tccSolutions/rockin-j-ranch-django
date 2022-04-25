import random
from django.shortcuts import render
from horse.models import Horse, Image, Medical
from django.views.decorators.clickjacking import xframe_options_exempt
from django.db.models import Q
from datetime import date

@xframe_options_exempt
def barn(request):
   
    horses = Horse.objects.all()
    for horse in horses:       
        horse_images = Image.objects.filter(Q(horse=horse) & Q(private_image=False))
       
         
        horse.age = date.today().year - horse.year_foaled
        try:
            horse.height = Medical.objects.filter(height__isnull=False, horse=horse).latest().height
        except:
            horse.height = "Will be measured soon"       
        if horse_images:            
                horse.image = random.choice(Image.objects.filter(horse=horse.id))
             
    context = {'horses':horses}
    return render(request, 'barn/barn.html', context)