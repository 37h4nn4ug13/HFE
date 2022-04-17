import re
from tkinter.messagebox import NO
from django.shortcuts import redirect, render, reverse
from .models import EventPicture, Slide, Event
from django.views.generic import ListView, DetailView
from .forms import NotifyForm, EventImageForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import user_passes_test
from django.views.generic.edit import FormMixin


# Create your views here.

def index(request):
    min = 1000
    for i in Slide.objects.all():
        if i.pk < min:
            min = i.pk

    context = {
        'slides': Slide.objects.all(),
        'min': min
    }
    return render(request, 'events/home.html', context)


class EventView(ListView):
    model = Event


class EventDetailView(FormMixin, DetailView):
    model = Event
    form_model = EventPicture
    form_class = EventImageForm
    def get_success_url(self):
        return reverse('event', kwargs={'pk': self.object.id})

    def get_context_data(self, **kwargs):
        context = super(EventDetailView, self).get_context_data(**kwargs)
        context['images'] = EventPicture.objects.all()
        context['form'] = EventImageForm(initial={'Event': self.object})
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        event = self.get_object()
        myform = form.save(commit=False)
        myform.event =  event
        form.save()
        return super(EventDetailView, self).form_valid(form)





@user_passes_test(lambda u: u.is_staff)
def notify_view(request):
    if request.method == "POST":
        form = NotifyForm(request.POST)
        if form.is_valid():
            import smtplib
            with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
                smtp.ehlo()
                smtp.starttls()
                smtp.ehlo()
                smtp.login('homeschoolformalevents@gmail.com', 'A135792468s')

                subject = form.cleaned_data['subject']
                body = form.cleaned_data['body']
                msg = f'Subject: {subject}\n\n{body}'
                for user in User.objects.all():
                    smtp.sendmail('homeschoolformalevetns@gmail.com', user.email, msg)
                return redirect('home')

    else:
        form = NotifyForm()
    
    context = {
        'form': form

    }
    return render(request, 'events/notify.html', context)