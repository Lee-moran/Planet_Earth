from .models import Comment, Post
from django_summernote.widgets import SummernoteWidget
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class BlogForm(forms.ModelForm):
    """
    Form to add a blog
    """
    class Meta:
        model = Post
        fields = [
            'title',
            'author',
            'content',
            'featured_image',
            'read_time',
            'rating',
        ]
        widgets = {
            'content': SummernoteWidget(),
        }

    def __init__(self, *args, **kwargs):
        super(BlogForm, self).__init__(*args, **kwargs)
