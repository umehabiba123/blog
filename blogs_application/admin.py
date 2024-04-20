from django.contrib import admin
from .models import Categorie,Blog

# Register your models here.
@admin.register(Categorie)

class CategoryAdminModel(admin.ModelAdmin):
    list_display = ["name","id"]
@admin.register(Blog)
class BlogAdminModel(admin.ModelAdmin):
    list_display = ["title","author","category","description","Create_date","tags","image"]