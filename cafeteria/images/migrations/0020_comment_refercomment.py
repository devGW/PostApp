# Generated by Django 2.2.1 on 2019-09-09 15:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0019_remove_comment_refercomment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='referComment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='commentOnComment', to='images.Comment'),
        ),
    ]
