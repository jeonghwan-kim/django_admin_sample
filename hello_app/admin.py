from django.contrib import admin

from .models import Resource

class ResourceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

admin.site.register(Resource, ResourceAdmin)

