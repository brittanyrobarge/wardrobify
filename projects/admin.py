from django.contrib import admin
from .models import Project

# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'description')
    search_fields = ('name', 'owner__username')

admin.site.register(Project, ProjectAdmin)
