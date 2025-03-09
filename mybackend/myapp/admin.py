from django.contrib import admin
from .models import Animal, Hall

@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    # 列表頁面只顯示「名稱」、「時段」、「物種」、「年齡」與「館別」
    list_display = ('name', 'time_slot', 'species', 'age', 'hall')
    search_fields = ('name', 'species', 'time_slot')
    # 編輯表單中僅包含這些欄位，不包含體重
    fields = ('name', 'time_slot', 'age', 'species', 'hall', 'photo')

@admin.register(Hall)
class HallAdmin(admin.ModelAdmin):
    list_display = ('name',)
