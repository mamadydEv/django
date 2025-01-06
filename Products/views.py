from django.shortcuts import render
from .models import *
from django.shortcuts import redirect


# Create your views here.


def home(request):
        category = Category.objects.filter(sub_cat=False)
        return render(request, 'home/home.html', {'category': category})


def all_product(request, slug=None, id=None):
        products = Product.objects.all()
        category = Category.objects.filter(sub_cat=False)
        if slug and id:
            data = Category.objects.get(slug=slug, id=id)
            products = products.filter(category=data)
        return render(request, 'home/products.html',
                  {'products': products, 'category': category})


def detail_product(request, id):
        products = Product.objects.get(id=id)
        similar = products.tags.similar_objects()[:4]
        is_like = False
        if products.like.filter(id=request.user.id).exists():
             is_like = True
        return render(request, 'home/detail.html', {'similar': similar, 'products': products , 'is_like' : is_like})


def like_product(request, id):
    url = request.META.get('HTTP_REFERER')
    products = Product.objects.get(id=id)
    if products.like.filter(id=request.user.id).exists():
        products.like.remove(request.user)
    else:
        products.like.add(request.user)
    return redirect(url)
# is_like = False
        # if products.like.filter(id=request.user.id).exists():
        #     is_like = True