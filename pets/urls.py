from django.urls import path

from . import views

app_name = 'pets'

urlpatterns = [
    path('', views.get_pets, name='pets'),
    path('<int:pk>/', views.get_pet_detail, name='pet_detail')
]
