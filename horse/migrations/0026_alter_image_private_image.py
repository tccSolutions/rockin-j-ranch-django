# Generated by Django 4.0.1 on 2022-02-09 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('horse', '0025_image_private_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='private_image',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
