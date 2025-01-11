from django.contrib import admin
from .models import *
# Register your models here.

class Cart_Admin(admin.ModelAdmin) :
    fields = ['quantity']
admin.site.register(Cart , Cart_Admin)