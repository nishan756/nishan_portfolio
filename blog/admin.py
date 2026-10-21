from django.contrib import admin

from .models import BlogPlaylist, BlogPlaylistRecord


@admin.register(BlogPlaylist)
class BlogPlaylistAdmin(admin.ModelAdmin):
    list_display = ["title", "priority"]
    list_editable = ["priority"]

@admin.register(BlogPlaylistRecord)
class BlogPlaylistRecordAdmin(admin.ModelAdmin):
    list_display = ["title", "playlist", "priority"]
    list_editable = ["priority"]