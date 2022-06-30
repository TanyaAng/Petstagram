from django.shortcuts import render

from petstagram.main.models import Profile, PetPhoto


def get_profile():
    profiles = Profile.objects.all()
    if profiles:
        return profiles[0]
    return None


def show_home(request):
    context = {
        'hide_additional_nav_items': True,
    }
    return render(request, 'home_page.html', context)


def show_dash_board(request):
    profile = get_profile()
    pet_photos = PetPhoto.objects.filter(tagged_pets__user_profile=profile)
    context = {
        'pet_photos': pet_photos,
    }
    return render(request, 'dashboard.html', context)


def show_profile(request):
    return render(request, 'profile_details.html')


def show_photo(request, pk):
    return render(request, 'photo_details.html')
