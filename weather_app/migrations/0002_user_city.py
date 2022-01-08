# Generated by Django 4.0.1 on 2022-01-07 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='city',
            field=models.CharField(choices=[(1, 'Mumbai'), (2, 'Delhi'), (3, 'Chennai'), (4, 'Bangalore'), (5, 'Kolkata')], default=5, max_length=15),
        ),
    ]