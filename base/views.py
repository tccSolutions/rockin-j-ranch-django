from django.shortcuts import render
from django.views.decorators.clickjacking import xframe_options_exempt



@xframe_options_exempt
def home(request):    
    return render(request, 'base/index.html')



