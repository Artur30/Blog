from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager


class Article(models.Model):

    class Meta:
        db_table = 'article'

    article_title = models.CharField(verbose_name='Заголовок', max_length=200)
    article_start_image = models.ImageField(verbose_name='Начальная картинка', upload_to='images/article/%Y/%m/%d',
                                            blank=True, null=True)
    article_start_text = models.TextField(verbose_name='Краткий текст')
    article_text = models.TextField(verbose_name='Содержимое статьи')
    article_date = models.DateTimeField(verbose_name='Дата и время')
    article_likes = models.IntegerField(verbose_name='Likes', default=0)
    article_author = models.CharField(verbose_name='Автор статьи', max_length=200)
    article_published = models.BooleanField(default=True)
    article_tags = TaggableManager(verbose_name='Теги', blank=True)

    users_likes = models.ManyToManyField(User, related_name='users_article_main')

    def __str__(self):
        return self.article_title


class Comments(models.Model):

    class Meta:
        db_table = 'comments'

    comments_text = models.TextField(verbose_name='Текст комментария')
    comments_date = models.DateTimeField()
    comments_article = models.ForeignKey(Article, on_delete=models.CASCADE)
    comments_from = models.ForeignKey(User, on_delete=models.CASCADE)



