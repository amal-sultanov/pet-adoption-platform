from django.core.paginator import Paginator
from django.shortcuts import render

from users.models import SelectedPetModel
from .models import (PetModel, PetTypeModel, PetBreedModel, PetSizeModel,
                     PetColorModel)


def get_pets(request):
    search_query = request.GET.get('search', '')
    type_query = request.GET.get('type', '')
    breed_query = request.GET.get('breed', '')
    size_query = request.GET.get('size', '')
    color_query = request.GET.get('color', '')
    pets = PetModel.objects.filter(quantity__gt=0)

    # search by exactly one of the following criteria
    if search_query:
        pets = pets.filter(
            type__type__icontains=search_query
        ) | pets.filter(
            breed__breed__icontains=search_query)
    elif type_query:
        pets = pets.filter(type=type_query)
    elif breed_query:
        pets = pets.filter(breed=breed_query)
    elif size_query:
        pets = pets.filter(size=size_query)
    elif color_query:
        pets = pets.filter(color=color_query)

    types = PetTypeModel.objects.all()
    breeds = PetBreedModel.objects.all()
    sizes = PetSizeModel.objects.all()
    colors = PetColorModel.objects.all()

    # pagination configuration, showing 15 pets on one page
    paginator = Paginator(pets, 15)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'types': types,
               'breeds': breeds,
               'sizes': sizes,
               'colors': colors,
               'page_obj': page_obj}

    return render(request, 'pets.html', context)


def get_pet_detail(request, pk):
    pet = PetModel.objects.get(id=pk)
    related_pets = PetModel.objects.filter(type=pet.type).exclude(id=pet.pk)
    # check whether user added the pet to 'selected pets'
    is_in_selected_pets = SelectedPetModel.objects.filter(
        user=request.user,
        pet=pet,
        is_adopted=False,
        quantity__gte=1).exists() if request.user.is_authenticated else False

    context = {'pet': pet,
               'related_pets': related_pets,
               'is_in_selected_pets': is_in_selected_pets}

    return render(request, 'pet-detail.html', context)
