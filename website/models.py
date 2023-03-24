from django.db import models

# Create your models here.

class Record(models.Model):
    dateCreated = models.DateTimeField(auto_now_add=True)
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zipCode = models.CharField(max_length=8)

    def __str__(self):
        return(f'{self.firstName} {self.lastName}')
    
