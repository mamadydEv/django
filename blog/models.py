from django.db import models

# Create your models here.

class Post(models.Model):
    STATUS_CHOICES = (
        ('pub' , 'published'),
        ('drf' , 'draft'),
    )
    label = models.CharField(max_length=100)
    caption = models.TextField()
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=STATUS_CHOICES , max_length=3)
    def __str__(self):
        return self.label
