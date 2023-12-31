from django.db import models

class ToDo(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    description = models.CharField(max_length=1000)
    category = models.CharField(max_length = 100)
    completed = models.BooleanField()