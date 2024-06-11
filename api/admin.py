from django.contrib import admin
from .models import *

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','created_at','updated_at']
    list_filter = ['name']
    list_per_page = 10
admin.site.register(Category,CategoryAdmin)


class BookAdmin(admin.ModelAdmin):
    list_display = ['name','description','date','price','discount','wrapper','page_number']
    list_filter = ['name','description']
    list_editable = ['price','discount','wrapper','page_number']
    list_per_page = 10
admin.site.register(Book,BookAdmin)

class ClientAdmin(admin.ModelAdmin):
    list_display = ['name','surname','address']
    list_filter = ['name','surname','address']
    list_per_page1 = 10

admin.site.register(Client, ClientAdmin)