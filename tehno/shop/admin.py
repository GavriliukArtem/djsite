from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


class ShopAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'get_photo', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {'slug': ('title',)}
    fields = ('title', 'slug', 'cat', 'content', 'specif', 'photo', 'get_photo', 'is_published')
    readonly_fields = ('time_create', 'time_update', 'get_photo')
    save_on_top = True

    def get_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width=70")

    get_photo.short_description = 'Photo'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Shop, ShopAdmin)
admin.site.register(Category, CategoryAdmin)
