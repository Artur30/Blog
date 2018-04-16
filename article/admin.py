from django.contrib import admin
from article.models import Article, Comments
from django_summernote.admin import SummernoteModelAdmin


class ArticleInLine(admin.StackedInline):

    model = Comments
    extra = 1


class ArticleAdmin(SummernoteModelAdmin):

    fields = ['article_title', 'article_start_image', 'article_start_text', 'article_date', 'article_text',
              'article_published', 'article_author']
    summernote_fields = ['article_text']
    inlines = [ArticleInLine]
    list_filter = ['article_date', 'article_author']
    list_display = ['article_title', 'article_date', 'article_author']


admin.site.register(Article, ArticleAdmin)





