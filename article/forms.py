from article.models import Comments, Article
from django import forms


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comments
        fields = ['comments_text']


class NewState(forms.ModelForm):

    class Meta:
        model = Article
        fields = ['article_title', 'article_text', 'article_image', 'article_video']





