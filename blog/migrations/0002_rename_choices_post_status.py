# Generated by Django 5.1.1 on 2024-10-19 20:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='choices',
            new_name='status',
        ),
    ]