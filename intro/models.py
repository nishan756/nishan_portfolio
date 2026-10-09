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
        queryset = Designation.objects.filter(title__iexact = self.name)
    
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

    description = SummernoteTextField()

    started_at = models.DateField()

    end_at = models.DateField(blank = True , null = True)

    class Meta:
        ordering = ["started_at"]