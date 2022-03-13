from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=30)
    number=models.PositiveIntegerField()
    email=models.EmailField()
    def __str__(self):
        return str(self.name)+"["+str(self.number)+']'
