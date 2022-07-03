from django.shortcuts import render, redirect

from petstagram.main.models import PetPhoto
from petstagram.main.views.helpers import get_profile


def show_home(request):
    context = {
        'hide_additional_nav_items': True,
    }
    return render(request=request, template_name='home_page.html', context=context)


def show_dash_board(request):
    profile = get_profile()
    pet_photos = PetPhoto.objects.prefetch_related('tagged_pets').filter(tagged_pets__user_profile=profile).distinct()
    context = {
        'pet_photos': pet_photos,
    }
    return render(request, 'dashboard.html', context)
