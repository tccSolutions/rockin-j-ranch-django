from django.contrib import admin

# Register your models here.
from .models import Medical, Trainer, Horse, Training,Image, Note

admin.site.register(Trainer)
admin.site.register(Horse)
admin.site.register(Training)
admin.site.register(Image)
admin.site.register(Note)
admin.site.register(Medical)