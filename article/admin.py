from django.contrib import admin
from article.models import Article, Comments, Image


class ArticleInLine(admin.StackedInline):

    model = Comments
    extra = 1


class ImageInLine(admin.StackedInline):

    model = Image
    extra = 1


class ArticleAdmin(admin.ModelAdmin):

    fields = ['article_title', 'article_text', 'article_date', 'article_video', 'article_published']
    inlines = [ImageInLine, ArticleInLine]
    list_filter = ['article_date']
    list_display = ['article_title', 'article_date']


admin.site.register(Article, ArticleAdmin)








