from django.contrib import admin

# Register your models here.
from .models import Trainer, Horse, Training

admin.site.register(Trainer)
admin.site.register(Horse)
admin.site.register(Training)