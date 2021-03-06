# Generated by Django 4.0 on 2022-01-03 02:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trainer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('bio', models.TextField(blank=True, max_length=1000, null=True)),
                ('age', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Horse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('breed', models.CharField(max_length=200)),
                ('bio', models.TextField(blank=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('training', models.TextField(blank=True, null=True)),
                ('sex', models.CharField(max_length=100)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('adoptable', models.BooleanField()),
                ('trainer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.trainer')),
            ],
        ),
    ]
