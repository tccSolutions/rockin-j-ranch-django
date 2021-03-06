# Generated by Django 4.0 on 2022-01-03 03:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.TextField()),
                ('comment', models.TextField(blank=True, null=True)),
                ('horse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.horse')),
            ],
        ),
    ]
