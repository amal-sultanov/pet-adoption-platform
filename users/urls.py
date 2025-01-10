from django.urls import path, include

from . import views

app_name = 'users'

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', views.registration_view, name='register'),
    path('logout', views.logout_view, name='logout'),
    path('add-to-selected-pets/<int:pk>/', views.add_to_selected_pets_view,
         name='add_to_selected_pets'),
    path('delete-from-selected-pets/<int:pk>/',
         views.delete_from_selected_pets_view,
         name='delete_from_selected_pets'),
    path('selected-pets/', views.selected_pets_view, name='selected_pets'),
    path('adopt/', views.adoption_view, name='adoption'),
    path('history/', views.history_view, name='history')
]
