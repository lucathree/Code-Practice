from django.contrib import admin

# Register your models here.
from .models import Garbage

@admin.register(Garbage)
class GarbageAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'admin')