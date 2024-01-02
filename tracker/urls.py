"""
URL configuration for tracker project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from accounts.views import user_login, user_logout, user_signup

from projects.views import create_project, list_projects, show_project
from tasks.views import create_task, list_tasks


def redirect_to_home(request):
    return redirect("home")


urlpatterns = [
    path("admin/", admin.site.urls),
    path("login/", user_login, name="login"),
    path("logout/", user_logout, name="logout"),
    path("signup/", user_signup, name="signup"),
    path("", list_projects, name="list_projects"),
    path("projects/", include("projects.urls")),
    path("accounts/", include("accounts.urls")),
    path("", redirect_to_home, name="home"),
    path("<int:id>/", show_project, name="show_project"),
    path("projects/create/", create_project, name="create_project"),
    # path("tasks/", include("tasks.urls")),
    path("tasks/create/", create_task, name="create_task"),
    path("tasks/mine/", list_tasks, name="show_my_tasks"),
]
