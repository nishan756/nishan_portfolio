from django.shortcuts import render, redirect

from .models import BlogPlaylist, BlogPlaylistRecord

from django.contrib import messages

def blog_playlists(request):

    playlists = BlogPlaylist.objects.all()

    context = {
        "playlists":playlists,
    }

    return render(request, "blog-playlist.html", context)


def blog_playlist_records(request, slug:str):

    try:

        playlist = BlogPlaylist.objects.get(slug = slug)

    except BlogPlaylist.DoesNotExist:

        messages.info(request, "Playlist not found")

        return redirect("blog-playlists")

    records = BlogPlaylistRecord.objects.filter(playlist = playlist)

    context = {
        "records":records,
        "playlist":playlist
    }

    return render(request, "playlist-records.html", context)

def record_detail(request, slug:str):

    try:

        record = BlogPlaylistRecord.objects.get(slug = slug)

    except BlogPlaylistRecord.DoesNotExist:

        messages.info(request, "OOPS! Record not found")

    return render(request, "record-detail.html" , {"record":record})