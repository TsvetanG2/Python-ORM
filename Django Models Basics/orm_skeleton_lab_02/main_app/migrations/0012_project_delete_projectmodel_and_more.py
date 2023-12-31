# Generated by Django 4.2.4 on 2023-10-31 06:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0011_alter_employee_birth_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('budget', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('duration_in_days', models.PositiveIntegerField(blank=True, null=True, verbose_name='Duration in Days')),
                ('estimated_hours', models.FloatField(blank=True, null=True, verbose_name='Estimated Hours')),
                ('start_date', models.DateField(blank=True, default=datetime.date.today, null=True, verbose_name='Start Date')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('last_edited_on', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.DeleteModel(
            name='ProjectModel',
        ),
        migrations.AlterField(
            model_name='department',
            name='employees_count',
            field=models.PositiveIntegerField(default=1, verbose_name='Employees Count'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='name',
            field=models.CharField(max_length=30),
        ),
    ]
