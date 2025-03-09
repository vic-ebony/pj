from django.contrib import admin
from .models import Animal, Hall

@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    # 更新為新的欄位名稱（size, fee）
    list_display = ('name', 'time_slot', 'size', 'fee', 'hall')
    search_fields = ('name', 'size', 'time_slot')
    # 修改 fields，確保不包含已刪除的欄位
    fields = ('name', 'time_slot', 'fee', 'size', 'hall', 'photo')

@admin.register(Hall)
class HallAdmin(admin.ModelAdmin):
    list_display = ('name',)
