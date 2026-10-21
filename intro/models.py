from django.db import models

from django.core.exceptions import ValidationError

from django_summernote.fields import SummernoteTextField

class Education(models.Model):
    title = models.CharField(max_length = 200)

    result = models.CharField(max_length = 10)

    institution = models.CharField(max_length = 100)

    started_at = models.DateField()

    end_at = models.DateField(blank = True , null = True)

    class Meta:
        ordering = ["started_at"] 

    def __str__(self):
        return self.title

class Designation(models.Model):
    title = models.CharField(max_length = 100)

    def clean(self):
        queryset = Designation.objects.filter(title__iexact = self.title)
    
        if self.pk:
            queryset = queryset.exclude(id = id)
    
        if queryset:
            raise ValidationError("Country with this name is already exists.")

    def __str__(self):
        return self.title

class Company(models.Model):
    name = models.CharField(max_length = 100)

    logo = models.ImageField(upload_to = "company_logo/" , blank = True , null = True)

    def __str__(self):
        return self.name
    
class WorkExperience(models.Model):
    designation = models.ForeignKey(Designation , on_delete = models.SET_NULL , null = True)

    company = models.ForeignKey(Company , on_delete = models.SET_NULL , null = True)

    description = models.TextField(blank = True, null = True)

    started_at = models.DateField()

    end_at = models.DateField(blank = True , null = True)

    class Meta:
        ordering = ["started_at"]

class Project(models.Model):

    title = models.CharField(max_length = 100)

    image = models.ImageField(upload_to = "work_images/",blank = True, null = True)

    short_description = models.TextField(blank = True, null = True)

    description = SummernoteTextField(blank = True, null = True)

    live_url = models.URLField(blank = True, null = True)

    github_repo_url = models.URLField(blank = True, null = True)


    def __str__(self):

        return self.title


class Skill(models.Model):

    name = models.CharField(max_length = 50)

    def __str__(self):

        return self.name

class Profile(models.Model):

    name = models.CharField(max_length = 100)

    image = models.ImageField(upload_to = "profile_images/",blank = True, null = True)

    tag_line = models.CharField(max_length = 200)

    phone = models.CharField(max_length = 15, unique = True)

    email = models.EmailField(unique = True)

    description = models.TextField(blank = True)

    is_active = models.BooleanField(default = True)

    def __str__(self):

        return self.name

class Social(models.Model):

    name = models.CharField(max_length = 20)

    url = models.URLField(unique = True)

    def __str__(self):
        return f"{self.name} - {self.url}"


class Message(models.Model):

    name = models.CharField(max_length = 100)

    email = models.EmailField()

    message = models.TextField()

    created_at = models.DateTimeField(auto_now_add = True)

    is_read = models.BooleanField(default = False)

    def __str__(self):

        return self.name