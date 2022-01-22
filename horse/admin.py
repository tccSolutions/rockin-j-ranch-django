from django.contrib import admin

# Register your models here.
from .models import Trainer, Horse, Training,Image

admin.site.register(Trainer)
admin.site.register(Horse)
admin.site.register(Training)
admin.site.register(Image)