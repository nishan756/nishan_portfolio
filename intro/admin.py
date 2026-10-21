from django.contrib import admin

from .models import Profile, WorkExperience, Project, Skill, Social, Designation, Company, Education, Message
# Register your models here.


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ["title",  "github_repo_url", "live_url"]

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ["title",  "institution"]

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ["name"]

@admin.register(Designation)
class DesignationAdmin(admin.ModelAdmin):
    list_display = ["title", ]

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ["name",  "tag_line", "phone", "email"]

@admin.register(Social)
class SocialAdmin(admin.ModelAdmin):
    list_display = ["name",  "url",]

@admin.register(WorkExperience)
class WorkExperienceAdmin(admin.ModelAdmin):
    list_display = ["designation",  "company", "started_at" , "end_at"]

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ["name",  "email", "is_read" ]
    list_filter = ["is_read"]