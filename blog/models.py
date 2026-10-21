from django.db import models

from django.utils.text import slugify

from django_summernote.fields import SummernoteTextField

class BlogPlaylist(models.Model):

    slug = models.SlugField(blank = True, null = True)

    title = models.CharField(max_length = 100)

    image = models.ImageField(upload_to = "blog_playlist_banners/" , blank = True , null = True)

    priority = models.PositiveIntegerField()

    created_at = models.DateTimeField(blank = True, null = True)

    def save(self, *args, **kwargs):

        if not self.slug:

            self.slug = slugify(self.title)

        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:

        ordering = ["priority"]
    

class BlogPlaylistRecord(models.Model):
    slug = models.SlugField(blank = True, null = True)

    playlist = models.ForeignKey(BlogPlaylist, on_delete = models.CASCADE)

    title = models.CharField(max_length = 200)

    image = models.ImageField(upload_to = "blog_images/",blank = True, null = True)

    description = SummernoteTextField()

    priority = models.PositiveIntegerField()

    created_at = models.DateTimeField(blank = True, null = True)

    def __str__(self):

        return self.title

    def save(self, *args, **kwargs):

        if not self.slug:

            self.slug = slugify(self.title)

        return super().save(*args, **kwargs)


    class Meta:

        ordering = ["priority"]
