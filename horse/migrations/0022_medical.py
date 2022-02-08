# Generated by Django 4.0.1 on 2022-02-08 10:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('horse', '0021_rename_date_created_note_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Medical',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(null=True)),
                ('height', models.FloatField(null=True)),
                ('weight', models.IntegerField(null=True)),
                ('exam_notes', models.TextField(null=True)),
                ('vet', models.CharField(max_length=500, null=True)),
                ('wormed', models.BooleanField(default=False)),
                ('coggins', models.BooleanField(default=False)),
                ('horse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='horse.horse')),
            ],
        ),
    ]
