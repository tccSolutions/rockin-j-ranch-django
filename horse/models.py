import uuid
from xmlrpc.client import Boolean
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
        ordering: ('priority')

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
    price = models.FloatField(null=True, blank=True)    

    def __str__(self):
        return self.name


class Medical(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateField(null=True, blank=True)
    height = models.FloatField(null=True, blank=True)    
    exam_notes = models.TextField(null=True, blank=True)
    vet = models.CharField(max_length=500, null=True, blank=True)
    wormed = models.BooleanField(default=False)
    coggins = models.BooleanField(default=False)
    horse = models.ForeignKey(Horse, on_delete=CASCADE)
    girth = models.FloatField(null=True, blank=True)
    length = models.FloatField(null=True, blank=True)
    red_tape = models.FloatField(null=True, blank=True)
    black_tape = models.FloatField(null=True, blank=True)

    class Meta:
        get_latest_by = 'date'
    

    def get_weight(red, black, girth, length):
        if red != None and black!= None and girth != None and length != None:
            gl_weight = round(((girth**2 ) * length)/300)
            return round((gl_weight + red + black)/3)
        else:
            return None

    def medical_encoder(medical):
        return {
            "name": medical.name,
            "date": str(medical.date),
            "height": medical.height,
            "weight": medical.weight,
            "exam_notes": medical.exam_notes,
            "vet": medical.vet,
            "wormed": medical.wormed,
            "coggins": medical.coggins,
            "horse": str(medical.horse)
        }

    def __str__(self):
        return f"{self.horse.name}-{self.name}-{self.date.strftime('%d %B, %Y')}"


class Image(models.Model):
    url = models.CharField(max_length=300)
    comment = models.CharField(max_length=300, null=True, blank=True)
    name = models.CharField(max_length=300)
    horse = models.ForeignKey(Horse, on_delete=CASCADE, null=True)
    private_image = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return f"{self.comment}-{self.url}"


class Note(models.Model):
    date = models.DateField()
    note = models.CharField(max_length=500)
    horse = models.ForeignKey(Horse, on_delete=CASCADE)

    def __str__(self):
        return self.note
