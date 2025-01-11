
from django.urls import  path
from . import views
app_name = 'cart'
urlpatterns = [
    path('add/<int:id_product>/' , views.add_order , name='add_order') ,
    path('remove/<int:id_product>/' , views.remove_order , name='remove_order'),
    path('detail/' , views.orders_detail , name = 'orders_detail' ),

]