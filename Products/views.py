from django.shortcuts import render
from .models import *
from django.shortcuts import redirect
from .forms import SearchForm
from django.db.models import Q



# Create your views here.


def home(request):
        category = Category.objects.filter(sub_cat=False)
        return render(request, 'home/home.html', {'category': category})


def all_product(request, slug=None, id=None):
        products = Product.objects.all()
        form = SearchForm()
        category = Category.objects.filter(sub_cat=False)
        if slug and id:
            data = Category.objects.get(slug=slug, id=id)
            products = products.filter(category=data)
        return render(request, 'home/products.html',
                  {'products': products, 'category': category , 'form' : form})


def detail_product(request, id):
        products = Product.objects.get(id=id)
        comment_form = commentform()
        replyForm = ReplyForm()
        images = Images.objects.filter(products_id=id)
        comment = Comment.objects.filter(product_id=id , is_reply=False)
        comments = Comment.objects.get(id=id)
        similar = products.tags.similar_objects()[:4]
        is_like = False
        if products.like.filter(id=request.user.id).exists():
             is_like = True
        is_like_comment = False
        if comments.like_comment.filter(id=request.user.id).exists():
            is_like_comment = True

        return render(request, 'home/detail.html', {'similar': similar, 'products': products ,
                                                    'is_like' : is_like ,
                                                    'comment_form' : comment_form ,
                                                    'comment' : comment ,
                                                    'replyForm' : replyForm ,
                                                    'is_like_comment' : is_like_comment ,
                                                    'images' : images
                                                    })


def like_product(request, id):
    url = request.META.get('HTTP_REFERER')
    products = Product.objects.get(id=id)
    if products.like.filter(id=request.user.id).exists():
        products.like.remove(request.user)
    else:
        products.like.add(request.user)
    return redirect(url)
def comment_form(request, id):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        Commentform = commentform(request.POST)
        if Commentform.is_valid():
            data = Commentform.cleaned_data
            Comment.objects.create(
                comment=data['comment'],
                rate= data['rate'],
                product_id=id,
                user_id=request.user.id
            )
    return redirect(url)
def reply(request,  id , comment_id):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        Commentform = ReplyForm(request.POST)
        if Commentform.is_valid():
            data = Commentform.cleaned_data
            Comment.objects.create(
                comment=data['comment']
                , product_id= id
                , user_id=request.user.id
                , reply_id = comment_id
                , is_reply=True
            )
            return redirect(url)
def like_comment(request , id) :
    url = request.META.get('HTTP_REFERER')
    comments = Comment.objects.get(id=id)
    if comments.like_comment.filter(id=request.user.id).exists():
        comments.like_comment.remove(request.user)
    else :
        comments.like_comment.add(request.user)
    return redirect(url)

def Searchform(request):
    products = Product.objects.all()
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data['content']
        if data.isdigit() :
            products = products.filter(Q(discount__exact=data) | Q(unit_price__exact=data) )
        else:
            products = products.filter(name__icontains=data)
        return render(request , 'home/products.html' , {'products' : products })