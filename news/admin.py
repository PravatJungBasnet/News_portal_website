from django.contrib import admin
from .models import Category,news
# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=['user','title','image']
@admin.register(news)
class newsAdmin(admin.ModelAdmin):
    list_display=['user','category','title','description','created_at']
