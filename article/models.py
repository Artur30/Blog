from django.db import models
from django.contrib.auth.models import User


class Article(models.Model):

    class Meta:
        db_table = 'article'

    article_title = models.CharField(verbose_name='Заголовок', max_length=200)
    article_text = models.TextField(verbose_name='Текст статьи')
    article_date = models.DateTimeField(verbose_name='Дата и время')
    article_likes = models.IntegerField(verbose_name='Likes', default=0)

    # article_image = models.ImageField(verbose_name='Картинка', upload_to='images/article/%Y/%m/%d',
    #                                   blank=True, null=True)
    article_video = models.FileField(verbose_name='Видео', upload_to='video/article/%Y/%m%d',
                                     blank=True, null=True)
    article_published = models.BooleanField(default=True)

    users_likes = models.ManyToManyField(User, related_name='users_article_main')

    def __str__(self):
        return self.article_title


class Image(models.Model):

    class Meta:
        db_table = 'image'

    image = models.ImageField(verbose_name='Картинка', upload_to='images/article/%Y/%m/%d',
                              blank=True, null=True)
    image_article = models.ForeignKey(Article, on_delete=models.CASCADE)


class Comments(models.Model):

    class Meta:
        db_table = 'comments'

    comments_text = models.TextField(verbose_name='Текст комментария')
    comments_date = models.DateTimeField()
    comments_article = models.ForeignKey(Article, on_delete=models.CASCADE)
    comments_from = models.ForeignKey(User, on_delete=models.CASCADE)



