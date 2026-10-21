from .models import Social, Profile

def social_links(request):

    profile = Profile.objects.filter(is_active = True).first()

    socials = Social.objects.all()

    return {"socials":socials, "profile":profile}