from django.contrib import admin
from .models import Category
from .models import CategoryField

# Register your models here.

class CategoryFieldInline(admin.TabularInline):
    model = CategoryField
    extra = 1

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines=[CategoryFieldInline]

#admin.site.register(Category)
#admin.site.register(CategoryField)