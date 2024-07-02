from django.contrib import admin
from .models import Post, Comment

# admin.site.register(Post)
# admin.site.register(Comment)


class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at")
    list_display_links = ["title"]
    search_fields = ["title"]


class CommentAdmin(admin.ModelAdmin):
    list_display = ("user", "created_at")


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
