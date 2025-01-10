from django.contrib.auth.models import User
from django.db import models

from pets.models import PetModel


class SelectedPetModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pet = models.ForeignKey(PetModel, on_delete=models.CASCADE)
    is_adopted = models.BooleanField(default=False)
    quantity = models.PositiveIntegerField()
    total_price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user}: {self.quantity} x {self.pet}'


class AdoptionModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=16)
    address = models.CharField(max_length=128)
    selected_pets = models.ManyToManyField(SelectedPetModel)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
