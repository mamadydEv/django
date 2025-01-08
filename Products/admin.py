from django.contrib import admin
from .models import *

# Register your models here.
class InlinesImages(admin.TabularInline) :
    model = Images
    extra = 3
class CategoryAdmin(admin.ModelAdmin) :
    list_display = ['name' , 'create' ,'update']
    prepopulated_fields = {
        'slug' : ('name' ,)
    }

class ProductAdmin(admin.ModelAdmin) :
    list_display = ['name','amount' ,'available' , 'unit_price' , 'discount' ,
                    'total_price']
    inlines = [InlinesImages]
class commentAdmin(admin.ModelAdmin) :
    list_display = ['user' , 'create' , 'rate']

admin.site.register(Category , CategoryAdmin)
admin.site.register(Product , ProductAdmin)
admin.site.register(Comment , commentAdmin)
admin.site.register(Images)