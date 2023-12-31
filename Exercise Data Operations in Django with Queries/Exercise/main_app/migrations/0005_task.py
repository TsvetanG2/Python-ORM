# Generated by Django 4.2.7 on 2023-11-11 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_car_alter_location_region'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25)),
                ('description', models.TextField()),
                ('due_date', models.DateField()),
                ('is_finished', models.BooleanField(default=False)),
            ],
        ),
    ]
