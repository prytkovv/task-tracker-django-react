from django.db import models


class Task(models.Model):
    text = models.CharField(max_length=300)
    day = models.DateField()
    reminder = models.BooleanField(default=False)
