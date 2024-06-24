from django.db import models

# Create your models here.

# models for activities or todos
class ToDo(models.Model):
    activity =models.CharField(max_length=255)

def __str__(self):
    return self.activity


# models for the login
class MemberLogin(models.Model):
    username= models.CharField(max_length=255, unique=True)
    password =models.CharField(max_length=100)
    email =models.EmailField(unique=True)

def __str__(self):
    return self.username

# models for the registration
class MemberRegistration(models.Model):
    firstName= models.CharField(max_length=255, unique=True)
    lastName= models.CharField(max_length=255, unique=True)
    email =models.EmailField(unique=True)
    password =models.CharField(max_length=100)
    comfirm_password =models.CharField(max_length=100)

def __str__(self):
    return self.firstName

    

    
