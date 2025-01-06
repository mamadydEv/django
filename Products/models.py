from django.db import models
from django.urls import reverse
from taggit.managers import TaggableManager
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    sub_category = models.ForeignKey('self', null='true', blank='true', on_delete=models.CASCADE, related_name='sub')
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
