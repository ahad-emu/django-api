from django.contrib import admin
from apps.models import SingerModel, SongModel

# Register your models here.
@admin.register(SingerModel)
class AdminSinger(admin.ModelAdmin):
    list_display = ['id', 'name', 'age', 'country']

@admin.register(SongModel)
class AdminSong(admin.ModelAdmin):
    list_display = ['id', 'title', 'singer']