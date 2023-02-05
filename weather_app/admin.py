from django.contrib import admin
from .models import History

# Register your models here.
class Weatheradmin(admin.ModelAdmin):
    list_display = ("city", "temperature", "date",)

admin.site.register(History, Weatheradmin)