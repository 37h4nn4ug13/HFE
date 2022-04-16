from distutils.command.upload import upload
from email.policy import default
from operator import mod
from pydoc import describe
from tkinter.tix import MAX
from django.db import models

# Create your models here.
class SlideShow(models.Model):
    title = models.CharField(max_length=80, null=True)
    description = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to="")

    def __str__(self):
        return self.title


class Event(models.Model):
    title = models.CharField(max_length=80)
    description = models.TextField()
    image = models.ImageField(upload_to='event_covers')
    date = models.DateField()
    has_happend = models.BooleanField(default=False)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-date']

