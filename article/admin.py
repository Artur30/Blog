from django.contrib import admin
from article.models import Article, Comments, Image
from django_summernote.admin import SummernoteModelAdmin


class ArticleInLine(admin.StackedInline):

    model = Comments
    extra = 1


class ArticleAdmin(SummernoteModelAdmin):

    fields = ['article_title', 'article_date', 'article_text', 'article_video', 'article_published']
    inlines = [ArticleInLine]
    list_filter = ['article_date']
    list_display = ['article_title', 'article_date']


admin.site.register(Article, ArticleAdmin)





