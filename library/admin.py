from django.contrib import admin
from library.models import Book

# Register your models here.
admin.site.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['id','title','datetime'] 