from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    completed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    