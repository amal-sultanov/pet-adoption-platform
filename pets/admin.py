from django.contrib import admin

from pets.models import (PetTypeModel, PetBreedModel, PetSizeModel,
                         PetColorModel, PetModel)

admin.site.register(PetTypeModel)
admin.site.register(PetBreedModel)
admin.site.register(PetSizeModel)
admin.site.register(PetColorModel)
admin.site.register(PetModel)
