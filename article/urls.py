from django.conf.urls import include, url
from article import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'article'

urlpatterns = [
    url(r'^articles/get/(?P<article_id>\d+)/(?P<comments_page_number>\d+)/$', views.article, name='article'),
    url(r'^articles/add_like/(?P<page_number>\d+)/(?P<article_id>\d+)/$', views.add_like, name='add_like'),
    url(r'^articles/add_comment/(?P<article_id>\d+)/$', views.add_comment, name='add_comment'),
    url(r'^articles/delete_likes/$', views.delete_likes, name='delete_likes'),
    url(r'^page/(?P<page_number>\d+)/$', views.articles, name='articles_page'),
    url(r'^suggest_article/$', views.suggest_article , name='suggest_article'),
    url(r'^', views.articles, name='articles'),
]



