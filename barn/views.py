from django.shortcuts import render
from horse.models import Horse, Image
# Create your views here.
def barn(request):
    horse_list = []
    horses = Horse.objects.all()
    for horse in horses:       
        new_horse = {
            'id': horse.id,
            'name': horse.name,
            'about': horse.bio[0:150],
            'adoptable': horse.adoptable,
            'image': Image.objects.filter(horse=horse.id).first()
        }
        horse_list.append(new_horse)  
    context = {'horses': horse_list}
    return render(request, 'barn/barn.html', context)