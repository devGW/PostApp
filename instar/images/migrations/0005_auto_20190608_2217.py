# Generated by Django 2.2.1 on 2019-06-08 13:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0004_auto_20190607_2340'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='Image',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='like',
            old_name='Image',
            new_name='image',
        ),
    ]
