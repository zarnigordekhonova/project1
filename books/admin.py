from django.contrib import admin
from books.models import Books, Books_description
# Register your models here.


admin.site.register(Books)
admin.site.register(Books_description)
