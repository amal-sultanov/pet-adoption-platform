from django.contrib import messages
from django.contrib.auth import logout, login
from django.contrib.auth.models import User
from django.shortcuts import redirect, render

from pets.models import PetModel
from .forms import RegistrationForm, AdoptionModelForm
from .models import SelectedPetModel, AdoptionModel


def registration_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            username = form.clean_username()
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password2')
            user = User.objects.create_user(username=username, email=email,
                                            password=password)

            user.save()
            login(request, user)

            return redirect('pages:homepage')

        context = {'form': form}
        return render(request, 'registration/registration.html', context)
    return render(request, 'registration/registration.html')


def logout_view(request):
    logout(request)

    return redirect('pages:homepage')


def add_to_selected_pets_view(request, pk):
    if request.method == 'POST':
        pet = PetModel.objects.get(id=pk)
        quantity = int(request.POST.get('quantity', 1))

        if pet.quantity >= quantity:
            total_price = pet.price * quantity

            SelectedPetModel.objects.create(user=request.user,
                                            pet=pet,
                                            quantity=quantity,
                                            total_price=total_price).save()

            return redirect('users:selected_pets')
        else:
            messages.error(request, 'Check available quantity!')
            return redirect('pets:pet_detail', pk=pet.id)


def delete_from_selected_pets_view(request, pk):
    pet = PetModel.objects.get(id=pk)
    SelectedPetModel.objects.filter(pet=pet).delete()

    return redirect('users:selected_pets')


def selected_pets_view(request):
    selected_pets = SelectedPetModel.objects.filter(user=request.user.id,
                                                    is_adopted=False)
    total = 0

    for pet in selected_pets:
        # final price for all selected pets
        total += pet.total_price

    context = {'selected_pets': selected_pets, 'total': total}

    return render(request, 'selected-pets.html', context)


def adoption_view(request):
    selected_pets = SelectedPetModel.objects.filter(user=request.user.id,
                                                    is_adopted=False)

    if request.method == 'POST':
        form = AdoptionModelForm(request.POST)

        if form.is_valid():
            adoption = form.save(commit=False)
            adoption.user = request.user
            adoption.save()
            adoption.selected_pets.set(selected_pets)

            for pet in selected_pets:
                pet.is_adopted = True
                # decrease the quantity of each pet being adopted in db
                pet.pet.quantity -= pet.quantity
                pet.save()
                pet.pet.save()

            return redirect('users:history')
        context = {'form': form}

        return render(request, 'adoption.html', context)

    total = 0

    for pet in selected_pets:
        # final price for all selected pets
        total += pet.total_price

    context = {'selected_pets': selected_pets, 'total': total}

    return render(request, 'adoption.html', context)


def history_view(request):
    adoptions = AdoptionModel.objects.filter(user=request.user)
    context = {'adoptions': adoptions}

    return render(request, 'history.html', context)
