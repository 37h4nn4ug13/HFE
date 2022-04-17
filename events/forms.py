from dataclasses import field
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import EventPicture


class NotifyForm(forms.Form):
    subject = forms.CharField(max_length=80)
    body = forms.CharField(widget=forms.Textarea)

class EventImageForm(forms.ModelForm):
    class Meta:
        model = EventPicture
        fields = ('image', )