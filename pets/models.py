from django.db import models


class PetTypeModel(models.Model):
    type = models.CharField(max_length=16)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.type


class PetBreedModel(models.Model):
    breed = models.CharField(max_length=64)
    type = models.ForeignKey(PetTypeModel, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.type}: {self.breed}'


class PetSizeModel(models.Model):
    SIZE_CHOICES = [
        ('Small', 'Small'),
        ('Medium', 'Medium'),
        ('Large', 'Large'),
        ('Extra Large', 'Extra Large'),
    ]
    size = models.CharField(max_length=16, choices=SIZE_CHOICES)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description


class PetColorModel(models.Model):
    color = models.CharField(max_length=16)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.color


class PetModel(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female')
    ]
    image = models.ImageField(upload_to='pets')
    name = models.CharField(max_length=16)
    type = models.ForeignKey(PetTypeModel, on_delete=models.CASCADE)
    breed = models.ForeignKey(PetBreedModel, on_delete=models.CASCADE)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    size = models.ForeignKey(PetSizeModel, on_delete=models.CASCADE)
    age = models.PositiveIntegerField()
    color = models.ForeignKey(PetColorModel, on_delete=models.CASCADE)
    description = models.TextField()
    price = models.FloatField()
    quantity = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.type}: {self.name}'
