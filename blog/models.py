from django.db import models

from django.utils.text import slugify

from django_summernote.fields import SummernoteTextField

from tinymce.models import HTMLField


def get_initial_playlist_priority():

    last_playlist = BlogPlaylist.objects.last()

    if last_playlist:

        return last_playlist.priority + 1

    return 0

class BlogPlaylist(models.Model):

    slug = models.SlugField(blank = True, null = True)

    title = models.CharField(max_length = 100)

    image = models.ImageField(upload_to = "blog_playlist_banners/" , blank = True , null = True)

    priority = models.PositiveIntegerField(default = get_initial_playlist_priority)

    created_at = models.DateTimeField(blank = True, null = True)

    def save(self, *args, **kwargs):

        if not self.slug:

            self.slug = slugify(self.title)

        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:

        ordering = ["priority"]



def get_initial_record_priority():

    last_record = BlogPlaylistRecord.objects.last()

    if last_record:

        return last_record.priority + 1

    return 0

class BlogPlaylistRecord(models.Model):
    slug = models.SlugField(blank = True, null = True)

    playlist = models.ForeignKey(BlogPlaylist, on_delete = models.CASCADE)

    title = models.CharField(max_length = 200)

    image = models.ImageField(upload_to = "blog_images/",blank = True, null = True)

    description = HTMLField()

    priority = models.PositiveIntegerField(default = get_initial_record_priority)

    class Status(models.TextChoices):

        DRAFT = "draft", "Draft"

        PUBLISHED = "published", "Published"

    status = models.CharField(max_length = 10, choices = Status.choices, default = Status.DRAFT)

    created_at = models.DateTimeField(blank = True, null = True)

    def __str__(self):

        return self.title

    def save(self, *args, **kwargs):

        if not self.slug:

            self.slug = slugify(self.title)

        return super().save(*args, **kwargs)


    class Meta:

        ordering = ["playlist", "priority"]

        unique_together = ["playlist","priority"]
