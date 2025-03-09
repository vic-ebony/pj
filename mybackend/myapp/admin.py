from django.contrib import admin
from .models import Animal, Hall

@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ('name', 'time_slot', 'size_display', 'fee', 'hall')
    search_fields = ('name', 'height', 'weight', 'cup_size', 'time_slot')
    fields = ('name', 'height', 'weight', 'cup_size', 'fee', 'time_slot', 'hall', 'photo')

@admin.register(Hall)
class HallAdmin(admin.ModelAdmin):
    list_display = ('name',)
