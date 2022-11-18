from django.contrib import admin
from .models import Video, Comment

# Register your models here.


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'uploader')
    ordering = ('title',)
    search_fields = ('title', 'uploader')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'video')
    ordering = ('video',)
