# Generated by Django 3.2.4 on 2021-08-15 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0008_donate'),
    ]

    operations = [
        migrations.CreateModel(
            name='Donorform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Donor_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('contact', models.IntegerField()),
                ('Donor_address', models.CharField(max_length=50)),
                ('restaurant_name', models.CharField(max_length=20)),
                ('restaurant_address', models.CharField(max_length=30)),
                ('TypeOfFood', models.CharField(max_length=50)),
                ('DateOfCooking', models.DateField()),
                ('Quantity', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=20)),
            ],
        ),
    ]