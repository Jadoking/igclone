# Generated by Django 2.2.2 on 2019-07-03 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0002_comment_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='caption',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]