from django.shortcuts import render

from pets.models import PetModel
from posts.models import PostModel
from .models import BannerModel, AboutModel


def homepage(request):
    banner = BannerModel.objects.first()
    about_section = AboutModel.objects.first()
    pets = PetModel.objects.all()[:5]
    posts = PostModel.objects.all().order_by('-created_at')[:2]

    context = {'banner': banner, 'about_section': about_section,
               'pets': pets, 'posts': posts}

    return render(request, 'index.html', context)
