from django.urls import include, path
from . import views
from .views import event_list

app_name = 'calendar_app'

urlpatterns = [
    path('event/<int:year>/<int:month>/<int:day>/', views.event, name='event'),
    path('event/<int:event_id>/', views.event_detail, name='event_detail'),
    path('event/create/', views.create_event, name='create_event'),
    path('event/edit/<int:event_id>/', views.edit_event, name='edit_event'),
    path('event/delete/<int:event_id>/', views.delete_event, name='delete_event'),
    path('events/', event_list, name='event_list'),
]
