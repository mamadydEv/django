from django.urls import path
from . import views

app_name = 'Products'
urlpatterns = [
    path('' , views.home , name = 'home') ,
    path('products/' ,views.all_product , name ='products'),
    path('category/<slug>/<int:id>/' , views.all_product , name = 'category'),
    path('products_detail/<int:id>/' , views.detail_product , name = 'detail_product'),
    path('like/<int:id>/' , views.like_product , name = 'like_product')
]