from django.urls import path
from . import views

app_name = 'job'

urlpatterns = [
   path('projects/<str:project_id>', views.projects, name='projects'),
   path('', views.main, name='main'),
]
