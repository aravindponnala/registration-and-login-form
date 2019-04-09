from django.db import models

# Create your models here.
class RegistrationData(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    mobile_no=models.BigIntegerField()
    email=models.EmailField(max_length=50)
    usernamed=models.CharField(max_length=50)
    passwordd=models.CharField(max_length=50)
    password2=models.CharField(max_length=50)

