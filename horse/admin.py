from django.contrib import admin

# Register your models here.
from .models import Trainer, Horse, Image

admin.site.register(Trainer)
admin.site.register(Horse)
admin.site.register(Image)