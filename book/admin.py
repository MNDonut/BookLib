from django.contrib import admin
from .models import Book, BookRate, Category
from bookmark.models import BookMark

class BookAdmin(admin.ModelAdmin):
    list_display = ['title' ,'number', 'get_author']

    # author is the foreign key field
    # it can't be displayed right in the list_display
    # so we create a method for displaying
    @admin.display(ordering='book__author', description='Автор')
    def get_author(self, obj):
        return obj.author

class BookRateAdmin(admin.ModelAdmin):
    list_display = ['book', 'numberOfOrders']

class BookMarkAdmin(admin.ModelAdmin):
    list_display = ['book', 'get_user']
    
    @admin.display(description='Користувач')
    def get_user(self, obj):
        return f'{obj.user.firstname} {obj.user.lastname} {obj.user.patronymic}'

admin.site.register(Book, BookAdmin)
admin.site.register(BookRate, BookRateAdmin)
admin.site.register(BookMark, BookMarkAdmin)
admin.site.register(Category)