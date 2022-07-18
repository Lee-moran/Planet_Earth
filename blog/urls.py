from . import views
from django.urls import path, include


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('like/<slug:slug>/', views.PostLike.as_view(), name='post_like'),
    path('your_blogs/', views.YourBlogs.as_view(), name='your_blogs'),
    path('add_blogs/', views.AddBlog.as_view(), name='add_blogs'),
    path('<slug:slug>/', views.PostDetails.as_view(), name='post_detail'),
]