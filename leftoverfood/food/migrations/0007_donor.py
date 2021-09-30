# Generated by Django 3.2.4 on 2021-08-13 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0006_agent_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Donor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=500)),
                ('contact', models.IntegerField()),
                ('restaurantname', models.CharField(max_length=50)),
                ('restaurantaddress', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
            ],
        ),
    ]
