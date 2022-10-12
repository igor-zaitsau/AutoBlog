from django.contrib import admin

from .models import *


class ArticlesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'time_create', 'is_published', 'author', 'category')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')


class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    list_display_links = ('title',)
    search_fields = ('title', 'slug')


admin.site.register(ArticleModel, ArticlesAdmin)
admin.site.register(CategoryModel, CategoriesAdmin)
