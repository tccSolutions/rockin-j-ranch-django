import uuid
from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

class Trainer(models.Model):
    name = models.CharField(max_length=200)
    bio = models.TextField(max_length=1000, null=True, blank=True)
    age = models.IntegerField(null=True)

    def __str__(self):
        return self.name

class Training(models.Model):   
   description = models.CharField(max_length=300)
   priority = models.IntegerField(null=True, blank=True)
   
   class Meta:
       ordering:('priority')
   def __str__(self):
       return self.description



class Horse(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=200)
    breed = models.CharField(max_length=200)
    bio = models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    training = models.ManyToManyField(Training)
    sex = models.CharField(max_length=100)
    year_foaled = models.IntegerField(null=True, blank=True)
    adoptable = models.BooleanField()
    trainer = models.ForeignKey(Trainer, on_delete=CASCADE)
    price = models.FloatField(null=True, blank=True )
    height= models.FloatField(null=True, blank=True)
    girth = models.FloatField(null=True, blank=True)
    length = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.name


class Image(models.Model):
    url = models.CharField(max_length=300)
    comment = models.CharField(max_length=300, null=True, blank=True)
    name = models.CharField(max_length=300)
    horse = models.ForeignKey(Horse, on_delete=CASCADE, null=True)

    def __str__(self):
        return self.url

class Note(models.Model):
    date_created = models.DateField()
    note = models.CharField(max_length=500)
    horse = models.ForeignKey(Horse, on_delete=CASCADE)

    def __str__(self):
        return self.note

