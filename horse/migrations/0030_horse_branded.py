# Generated by Django 4.0.3 on 2022-06-21 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('horse', '0029_horse_brand'),
    ]

    operations = [
        migrations.AddField(
            model_name='horse',
            name='branded',
            field=models.BooleanField(default=False),
        ),
    ]