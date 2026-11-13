from django.urls import path
from . import views

app_name = 'university'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('about/contacts/', views.contacts_view, name='contacts'),
    path('about/location/', views.location_view, name='location'),
    path('programs/', views.programs_view, name='programs'),
    path('timetable/', views.timetable_view, name='timetable'),
]
