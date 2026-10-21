from .views import blog_playlists, blog_playlist_records, record_detail

from django.urls import path

urlpatterns = [
    path("playlists/", blog_playlists, name = "blog-playlists"),

    path("playlist-records/<str:slug>/", blog_playlist_records, name = "playlist-records"),

    path("record/<str:slug>/", record_detail, name = "record-detail"),
]
