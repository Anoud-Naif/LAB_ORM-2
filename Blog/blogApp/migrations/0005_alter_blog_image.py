# Generated by Django 4.2.7 on 2023-11-25 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogApp', '0004_blog_category_blog_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(default='image/default.jpeg', upload_to='image/'),
        ),
    ]
