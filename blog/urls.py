from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('detail/<int:id>/' , views.detail , name='detail'),
    path('new_post/' , views.new_post , name='new_post' ),
    path('' , views.post_show , name='post_show'),
    path('update/<int:id>/' , views.update_post , name = 'up'),
    path('delete/<int:id>/' , views.delete_post , name = 'del')
]