# Generated by Django 2.0.4 on 2018-04-12 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0026_auto_20180412_1517'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/article/%Y/%m/%d', verbose_name='Картинка'),
        ),
        migrations.AlterField(
            model_name='article',
            name='article_video',
            field=models.FileField(blank=True, null=True, upload_to='video/article/%Y/%m%d', verbose_name='Видео'),
        ),
    ]
