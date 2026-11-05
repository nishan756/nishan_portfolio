from django.contrib import admin

from .models import BlogPlaylist, BlogPlaylistRecord


@admin.register(BlogPlaylist)
class BlogPlaylistAdmin(admin.ModelAdmin):
    list_display = ["title", "priority"]
    list_editable = ["priority"]

@admin.register(BlogPlaylistRecord)
class BlogPlaylistRecordAdmin(admin.ModelAdmin):
    list_display = ["title", "playlist", "priority", "status"]
    list_editable = ["priority"]
    actions = ["mark_selected_record_as_published", "mark_selected_record_as_draft"]

    def mark_selected_record_as_published(self, request, queryset):

        count = queryset.update(status = "published")

        return self.message_user(request, f"{count} records were marked as published.")

    def mark_selected_record_as_draft(self, request, queryset):

        count = queryset.update(status = "draft")

        return self.message_user(request, f"{count} records were marked as draft.")