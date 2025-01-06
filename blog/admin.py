from django.contrib import admin

# Register your models here.
from .models import Post

class Post_admin(admin.ModelAdmin) :
    list_display = ('status' , 'time_create' , 'time_update' , 'label')
admin.site.register(Post , Post_admin)