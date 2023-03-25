from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Record(models.Model):
    dateCreated = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='profile_pics', blank=True)
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    city = models.CharField(max_length=200)
    education = models.CharField(max_length=200)
    experience = models.CharField(max_length=200)
    skills = models.CharField(max_length=200)


    def __str__(self):
        return(f'{self.firstName} {self.lastName}')
    


class Actions(models.Model):
    dateCreated = models.DateTimeField(auto_now_add=True)
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=50)

    def __str__(self):
        return(f'{self.user} {self.action}')
    
