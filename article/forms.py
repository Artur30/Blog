from article.models import Comments, Article, Image
from django import forms


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comments
        fields = ['comments_text']


class NewState(forms.ModelForm):

    class Meta:
        model = Article
        fields = ['article_title', 'article_text', 'article_video']


class ImageForm(forms.ModelForm):

    class Meta:
        model = Image
        fields = ['image']
    image_img = forms.ImageField(label='Картинка')




