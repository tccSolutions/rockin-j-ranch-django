# Generated by Django 4.0.1 on 2022-02-06 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('horse', '0019_alter_horse_training'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='date_created',
            field=models.DateField(),
        ),
    ]
