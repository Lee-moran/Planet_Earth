from django.shortcuts import render
from django.views import generic
from .models import Post

# Create your views here.

'''
class based views - allow us to make
resuable views which inherit from each other
allows us yo view our blog
MVT - model,view,teplates
'''

class PostList (generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6


