from django.contrib import admin
from .models import Post, Comment, Tag
from django.utils.safestring import mark_safe


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'message', 'photo_tag',
                    'message_lenght', 'create_at', 'update_at', 'is_pubilc']
    list_display_links = ['message']
    list_filter = ['create_at', 'is_pubilc']
    search_fields = ['message']

    def photo_tag(self, post):
        if post.photo:
            return mark_safe(f'<img src="{post.photo.url}" style ="width:72px"/>')
        return None

    def message_lenght(self, post):
        return len(post.message)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass


@admin.register(Tag)
class TagAdmon(admin.ModelAdmin):
    pass
