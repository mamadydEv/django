from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = ([
    path('admin/', admin.site.urls),
    path('' , include('blog.urls' , namespace='blog')),
    path('accounts/' , include('accounts.urls' , namespace='accounts')),
    path('Products/' , include('Products.urls' , namespace='Products')),
    path('cart/', include('cart.urls', namespace='cart'))
               ]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)+
               static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))
