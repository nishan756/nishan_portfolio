from django.shortcuts import render, redirect

from .models import Project, WorkExperience, Education, Message

from .forms import MessageForm


def home(request):

    recent_projects = Project.objects.all()[:4]

    educations = Education.objects.all()

    context = {
        "recent_projects":recent_projects,
        "educations":educations
    }

    return render(request, "index.html", context)


def projects(request):

    all_projects = Project.objects.all()

    return render(request, "projects.html", {"projects":all_projects})

def about(request):

    experiences = WorkExperience.objects.all()


    context = {
        "experiences":experiences,
    }

    return render(request, "about.html", context)


def contact(request):

    form = MessageForm()

    if request.method == "POST":

        form = MessageForm(data = request.POST)

        if form.is_valid():

            form.save()

            return redirect("contact")

    return render(request, "contact.html")