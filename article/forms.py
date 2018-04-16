from article.models import Comments, Article
from django import forms
from django_summernote.widgets import SummernoteWidget


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comments
        fields = ['comments_text']


class NewState(forms.ModelForm):

    class Meta:
        model = Article
        fields = ['article_title', 'article_start_image', 'article_start_text', 'article_text']
        widgets = {
            'article_text': SummernoteWidget(),
        }

