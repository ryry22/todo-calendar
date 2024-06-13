from django.urls import path
from . import views

app_name = 'calendar_app'

urlpatterns = [
    path('calendar/', views.calendar, name='calendar'),
    path('calendar/<int:year>/<int:month>/', views.calendar, name='calendar'),
    path('event/<int:year>/<int:month>/<int:day>/', views.event, name='event'),
    path('event/<int:event_id>/', views.event_detail, name='event_detail'),
    path('event/create/', views.create_event, name='create_event'),
    path('event/<int:year>/<int:month>/<int:day>/<int:event_id>/edit/', views.event_edit, name='event_edit'),
    path('event/delete/<int:event_id>/', views.delete_event, name='delete_event'),
    path('events/', views.event_list, name='event_list'),
    path('events/<int:event_id>/delete/', views.delete_event, name='delete_event'),
]