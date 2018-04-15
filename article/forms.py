from article.models import Comments, Article, Image
from django import forms
from django_summernote.widgets import SummernoteWidget


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comments
        fields = ['comments_text']


class NewState(forms.ModelForm):

    class Meta:
        model = Article
        fields = ['article_title', 'article_text']
        widgets = {
            'article_text': SummernoteWidget(),
        }

