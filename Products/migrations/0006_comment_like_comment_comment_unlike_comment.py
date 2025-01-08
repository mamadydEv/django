# Generated by Django 5.1.1 on 2025-01-07 10:20

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0005_comment'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='like_comment',
            field=models.ManyToManyField(blank=True, related_name='like_comment', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comment',
            name='unlike_comment',
            field=models.ManyToManyField(blank=True, related_name='unlike_comment', to=settings.AUTH_USER_MODEL),
        ),
    ]