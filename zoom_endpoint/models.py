from django.db import models

from api.models import User, CourseCycle
# Create your models here.

class ClassMeetings(models.Model):
    course_cycle = models.OneToOneField(CourseCycle, primary_key=True, on_delete=models.CASCADE)
    mn = models.CharField(null=True, max_length=20)
    start_time = models.DateTimeField(null=True)
    end_time= models.DateTimeField(null=True)
    date_created = models.DateTimeField(auto_now_add=True)

class ClassMeetingsRecords(models.Model):
    course_cycle = models.OneToOneField(CourseCycle, primary_key=True, on_delete=models.CASCADE)
    mn = models.CharField(null=True, max_length=20)
    start_time = models.DateTimeField(null=True)
    end_time= models.DateTimeField(null=True)
    participants = models.JSONField(null=True)
    host = models.JSONField(null=True)
    date_created = models.DateTimeField(auto_now_add=True)