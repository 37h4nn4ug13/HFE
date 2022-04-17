from django.contrib import admin
from .models import Slide, Event, EventPicture

# Register your models here.
admin.site.register(Slide)
admin.site.register(Event)
admin.site.register(EventPicture)

fields = ( 'image_tag', )
readonly_fields = ('image_tag',)