from django.urls import path
from .views import list_projects, show_project

app_name = 'projects'

urlpatterns = [
    path('', list_projects, name="list_projects"),
    path('<int:id>/', show_project, name='show_project'),
]
