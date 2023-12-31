# Generated by Django 4.2.7 on 2023-11-04 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_eventregistration'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=30)),
                ('customer_name', models.CharField(max_length=100)),
                ('order_date', models.DateField()),
                ('status', models.CharField(choices=[('P', 'Pending'), ('Cpd', 'Completed'), ('Cnd', 'Cancelled')], max_length=30)),
                ('amount', models.PositiveIntegerField(default=1)),
                ('product_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total_price', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('warranty', models.CharField(default='No warranty', max_length=100)),
                ('delivery', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('age', models.PositiveIntegerField()),
                ('age_group', models.CharField(default='No age group', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Smartphone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, default=1, max_digits=10)),
                ('category', models.CharField(default='empty', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('age', models.PositiveIntegerField()),
                ('grade', models.CharField(max_length=10)),
                ('date_of_birth', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('contact_person', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(max_length=20, unique=True)),
                ('address', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='shoe',
            name='brand',
            field=models.CharField(max_length=25),
        ),
    ]
