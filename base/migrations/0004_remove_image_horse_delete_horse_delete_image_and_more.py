# Generated by Django 4.0 on 2022-01-03 16:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_horse_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='horse',
        ),
        migrations.DeleteModel(
            name='Horse',
        ),
        migrations.DeleteModel(
            name='Image',
        ),
        migrations.DeleteModel(
            name='Trainer',
        ),
    ]