from  django.urls import path

from event import views

urlpatterns = [
    path('events/', views.event, name="events"),
    path('event-details/', views.event_details, name="event-details")
]