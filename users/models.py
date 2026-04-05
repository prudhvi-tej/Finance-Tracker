from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    Role_choices=[
        ('viewer','Viewer'),
        ('analyst','Analyst'),
        ('admin','Admin'),
    ]
    role=models.CharField(max_length=10,choices=Role_choices,default='viewer')
    
