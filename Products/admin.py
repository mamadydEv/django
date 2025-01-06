from django.contrib import admin
from .models import *

# Register your models here.
class CategoryAdmin(admin.ModelAdmin) :
    list_display = ['name' , 'create' ,'update']
    prepopulated_fields = {
        'slug' : ('name' ,)
    }

class ProductAdmin(admin.ModelAdmin) :
    list_display = ['name','amount' ,'available' , 'unit_price' , 'discount' ,
                    'total_price']


admin.site.register(Category , CategoryAdmin)
admin.site.register(Product , ProductAdmin)
