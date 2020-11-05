from django.contrib import admin
from django.utils.safestring import mark_safe


from .models import *


class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    save_as = True
    #перечень полей которые видно в админке при просмотре списка книг
    list_display = ('id', 'title', 'slug', 'author', 'category', 'content', 'created_at', 'get_photo', 'town', 'type', 'owner')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    #перечеь полей по которым в админке организовывается фильтрация
    list_filter = ('category', 'genres')
    save_on_top = True
    readonly_fields = ('views', 'created_at', 'get_photo')
    #перечень полей которые показывает админка при добавлении новой книги
    fields = ('title', 'slug', 'author', 'genres', 'category', 'content', 'photo', 'get_photo', 'owner', 'town', 'type')

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="50"')
        return '-'
    get_photo.short_description = 'миниатюра'


class GenreAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


class TownAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


class TypeAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


class OwnerAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}



admin.site.register(Category, CategoryAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Type, TypeAdmin)
admin.site.register(Town, TownAdmin)
admin.site.register(Owner, OwnerAdmin)


#добавляем в админку раздел комментариев
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'book', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body')