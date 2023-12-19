from django.urls import path
from .views import list_projects

app_name = 'projects'

urlpatterns = [
    path('', list_projects, name='list_projects'),
]
