from django.urls import path
from . import views

app_name = 'app_experience'

urlpatterns = [
    path('', views.experience_list, name='experience_list'),
]