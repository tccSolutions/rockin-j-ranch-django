# Generated by Django 4.0.1 on 2022-02-06 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('horse', '0018_note'),
    ]

    operations = [
        migrations.AlterField(
            model_name='horse',
            name='training',
            field=models.ManyToManyField(to='horse.Training'),
        ),
    ]