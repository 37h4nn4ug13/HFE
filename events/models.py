from distutils.command.upload import upload
from email.policy import default
from operator import mod
from pydoc import describe
from time import timezone
from tkinter.tix import MAX
from django.db import models

# Create your models here.
class Slide(models.Model):
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
    price = models.FloatField()
    has_happend = models.BooleanField(default=False)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-date']

class EventPicture(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='event_pictures')
    date = models.DateField(null=True)

    def __str__(self):
        return self.event.title + str(self.pk)

    def image_tag(self):
        from django.utils.html import escape
        return u'<img src="%s" />' % escape(self.image.url)
    image_tag.short_description = 'Image'
    image_tag.allow_tags = True
