# Generated by Django 4.0.1 on 2022-02-09 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('horse', '0024_medical_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='private_image',
            field=models.BooleanField(default=False),
        ),
    ]
