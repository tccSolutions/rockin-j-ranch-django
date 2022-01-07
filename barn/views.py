import random
from django.shortcuts import render
from horse.models import Horse, Image
# Create your views here.
def barn(request):
   
    horses = Horse.objects.all()
    for horse in horses:       
        horse.image = random.choice(Image.objects.filter(horse=horse.id))
       
    context = {'horses':horses}
    return render(request, 'barn/barn.html', context)