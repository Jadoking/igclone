# Generated by Django 2.2.2 on 2019-07-03 06:26

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0004_post_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=models.ImageField(storage=django.core.files.storage.FileSystemStorage(location='media/posts/'), upload_to=''),
        ),
    ]
