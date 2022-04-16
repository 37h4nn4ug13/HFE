from django.urls import path
from . import views as event_views

urlpatterns = [
    path('', event_views.EventView.as_view(template_name="events/events.html"), name="events"),
    path('<pk>', event_views.EventDetailView.as_view(template_name="events/detail_event.html"), name='event')
]
