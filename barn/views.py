import random
from django.shortcuts import render
from horse.models import Horse, Image
from django.views.decorators.clickjacking import xframe_options_exempt

@xframe_options_exempt
def barn(request):
   
    horses = Horse.objects.all()
    for horse in horses: 
        horse_images = Image.objects.filter(horse=horse.id);
        if horse_images:      
            horse.image = random.choice(Image.objects.filter(horse=horse.id))
           
    context = {'horses':horses}
    return render(request, 'barn/barn.html', context)