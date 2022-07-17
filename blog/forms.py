from .models import Comment, Post
from django import forms
from django_summernote.widgets import SummernoteInplaceWidget


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class BlogForm(forms.ModelForm):
    """
    Form to add a recipe
    """
    class Meta:
        model = Post
        fields = [
            'title',
            'author',
            'excerpt',
            'featured_image',
        ]

        widgets = {
            'exerpt': SummernoteInplaceWidget()
        }

    def __init__(self, *args, **kwargs):
        super(BlogForm, self).__init__(*args, **kwargs)