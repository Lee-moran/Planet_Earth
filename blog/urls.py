from . import views
from django.urls import path, include


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('all_blogs', views.AllBlogs.as_view(), name='all_blogs'),
    path('summernote/', include('django_summernote.urls')),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('like/<slug:slug>', views.BlogLikes.as_view(), name='blog_likes'),
    path('your_blogs', views.YourBlogs.as_view(), name='your_blogs'),
    path('add_blogs', views.AddBlog.as_view(), name='add_blogs'),
    path('like/<slug:slug>', views.BlogLikes.as_view(), name='blog_like'),
]