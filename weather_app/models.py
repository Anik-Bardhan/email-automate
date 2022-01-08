from django.db import models
import datetime
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
import json, urllib.request

# Create your models here.

cities = (
    ('Mumbai', 'Mumbai'),
    ('Delhi', 'Delhi'),
    ('Chennai', 'Chennai'),
    ('Bangalore', 'Bangalore'),
    ('Kolkata', 'Kolkata'),
)

class User(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=15, choices=cities, default=5)
    createdAt = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return self.email

@receiver(post_save, sender=User)
def sendEmail(sender, instance, created, *args, **kwargs):
    if created:
        print(instance.email)
        city = instance.city
        source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' + city + '&units=metric&appid=8de66efbd0bab33e76ac6f192b178f47').read()

        list_of_data = json.loads(source)

        temp = str(list_of_data['main']['temp']) + ' °C'
        icon = list_of_data['weather'][0]['icon']

        html = f'''
            <html>
                <body>
                    <p>{city} : {temp}</p>
                    <img src="http://openweathermap.org/img/w/{icon}.png"/>
                </body>
            </html>
        '''
        subject = f'Hi {instance.name}, interested in our services.'
        message = ''
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [instance.email]
        send_mail(subject, message, email_from, recipient_list, html_message=html, fail_silently=False)    