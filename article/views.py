from django.shortcuts import render, render_to_response, get_object_or_404, redirect, reverse
from django.http import HttpResponse, Http404
from django.template.loader import get_template
from django.template import Context
from article.models import Article, Comments
from article.forms import CommentForm
from django.template.context_processors import csrf
from django.contrib import auth
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.utils import timezone
from blog import settings


def articles(request, page_number=1):
    all_articles = Article.objects.all()
    current_page = Paginator(all_articles, per_page=settings.Number_Articles_On_Page)
    articles_page = current_page.page(page_number)
    username = auth.get_user(request).username

    return render_to_response('article/articles.html', {'articles': articles_page, 'username': username})


def article(request, article_id=1, comments_page_number=1):
    comment_form = CommentForm
    args = {}
    args.update(csrf(request))
    args['article'] = Article.objects.get(id=article_id)
    args['comments'] = Comments.objects.filter(comments_article_id=article_id)
    args['form'] = comment_form
    args['username'] = auth.get_user(request).username

    # Пагинация комментариев
    current_comments_page = Paginator(args['comments'], per_page=settings.Number_Comments_On_Page)
    args['comments'] = current_comments_page.page(comments_page_number)

    return render_to_response('article/article.html', args)


"""
def add_like(request, article_id):
    if article_id in request.COOKIES:
        return redirect(reverse('article:articles'))
    else:
        article = get_object_or_404(Article, pk=article_id)
        article.article_likes += 1
        article.save()
        response = redirect(reverse('article:articles'))
        response.set_cookie(article_id, 'cookie')
        return response
"""


def add_like(request, page_number, article_id):
    all_articles = Article.objects.all()
    current_page = Paginator(all_articles, per_page=2)
    articles_page = current_page.page(page_number)
    username = auth.get_user(request).username

    if request.user.is_authenticated:
        users = User.objects.filter(users_article_main=article_id)
        current_user = request.user

        if current_user not in users:
            article = get_object_or_404(Article, pk=article_id)
            article.article_likes += 1
            article.users_likes.add(current_user)
            article.save()
    return render_to_response('article/articles.html', {'articles': articles_page, 'username': username})


def add_comment(request, article_id):
    if request.POST and ('pause' not in request.session):
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.comments_article = Article.objects.get(id=article_id)
            comment.comments_date = timezone.now()

            if request.user.id:
                comment.comments_from_id = request.user.id
            else:
                return HttpResponse('Не авторизован')

            form.save()
            # Создаем объект сессии в течении 60 секунд
            # request.session.set_expiry(60)
            # request.session['pause'] = True
    return redirect(reverse('article:article', args=(article_id, 1)))


def delete_likes(request):
    """ Удаление всех лайков на всех статьях """

    articles = Article.objects.all()

    for article in articles:
        article.article_likes = 0
        article.users_likes.clear()
        article.save()
    return redirect(reverse('article:articles'))






















