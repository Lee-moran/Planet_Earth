from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """
    Use Summernote for Blog admin
    """
    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content')
    actions = ['approve_posts']

    def approve_posts(self, request, queryset):
        """
        approval of comments
        """
        queryset.update(approved=True)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Ability to manage comments in admin panel
    """
    list_display = ('name', 'body', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ['name', 'email', 'body']
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        """
        approval of comments
        """
        queryset.update(approved=True)
