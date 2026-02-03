from django.db import models

# Create your models here.

class Courses(models.Model):
    title = models.CharField(max_length=255)
    code = models.CharField(unique=True)
    duration_weeks = models.IntegerField()

    def __str__(self):
        return self.title