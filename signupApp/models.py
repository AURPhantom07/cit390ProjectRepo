from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class RegisterCourse(models.Model):
   studentID=models.IntegerField(null=False, default=000000)
   firstName=models.CharField(max_length=250, null=False, default='')
   lastName=models.CharField(max_length=250, null=False, default='')   
   courseCode="cit390"
   term="Summer C, 2025"
   date=models.DateTimeField(default=timezone.now)

   def __str__(self):
      return self.username

