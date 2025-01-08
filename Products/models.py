from django.db import models
from django.urls import reverse
from taggit.managers import TaggableManager
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.db.models import Avg

# Create your models here.
class Category(models.Model):
    sub_category = models.ForeignKey('self', null='true', blank='true',
                                     on_delete=models.CASCADE, related_name='sub')
    sub_cat = models.BooleanField(default=False)
    name = models.CharField(max_length=100)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    slug = models.SlugField(allow_unicode=True, unique=True, blank=True, null=True)
    image = models.ImageField(upload_to='Category', null=True, blank=True)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('Products:category', args=[self.slug , self.id])

class Product(models.Model):
    category = models.ManyToManyField(Category, blank=True)
    name = models.CharField(max_length=100)
    amount = models.PositiveSmallIntegerField()
    unit_price = models.PositiveIntegerField()
    discount = models.PositiveSmallIntegerField(blank=True, null=True)
    total_price = models.PositiveIntegerField()
    information = models.TextField(blank=True, null=True)
    create = models.DateTimeField(auto_now_add=True)
    tags = TaggableManager(blank=True)
    update = models.DateTimeField(auto_now=True)
    available = models.BooleanField(default=True)
    image = models.ImageField(upload_to='Product')
    like = models.ManyToManyField(User , blank = True , related_name='like')
    unlike = models.ManyToManyField(User ,blank = True , related_name = 'unlike')
    total_like = models.PositiveSmallIntegerField()
    total_unlike = models.PositiveSmallIntegerField()

    def average(self):
        data = Comment.objects.filter(is_reply=False , product=self).aggregate(a = Avg('rate'))
        star = 0
        if data['a'] is not None :
            star = round(data['a'] , 1)
        return star
    def total_like(self):
        return self.like.count()
    def total_unlike(self):
        return self.unlike.count()
    @property
    def total_price(self):

        if not self.discount:
            return self.unit_price
        elif self.discount:
            total = (self.discount * self.unit_price) / 100
            return int(self.unit_price - total)
        return self.total_price
class Comment(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    product = models.ForeignKey(Product , on_delete=models.CASCADE)
    comment = models.TextField()
    reply = models.ForeignKey('self' , on_delete=models.CASCADE , null=True , blank=True , related_name='comment_reply')
    rate = models.PositiveSmallIntegerField(default = 1)
    create = models.DateTimeField(auto_now_add=True)
    is_reply = models.BooleanField(default = False)
    like_comment = models.ManyToManyField(User , blank = True , related_name='like_comment')
    unlike_comment = models.ManyToManyField(User ,blank = True , related_name = 'unlike_comment')
    total_like_comment = models.PositiveSmallIntegerField()
    total_unlike_comment = models.PositiveSmallIntegerField()
    def total_like_comment(self):
        return self.like_comment.count()

    def total_unlike_comment(self):
        return self.unlike_comment.count()
    def __str__(self):
        return self.product.name

class commentform(ModelForm):
    class Meta:
        model = Comment
        fields = ('comment', 'rate')
class ReplyForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)

class Images(models.Model) :
    products = models.ForeignKey(Product , on_delete=models.CASCADE)
    name = models.CharField(max_length=100 , blank=True)
    images = models.ImageField(upload_to='Gallery')

    def __str__(self):
        return self.products.name