# Generated by Django 5.0.1 on 2024-01-10 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_news'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='image',
            field=models.ImageField(default='2024-01-09 12:44', upload_to='news_img'),
            preserve_default=False,
        ),
    ]