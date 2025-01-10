from django.urls import path

from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.get_posts, name='posts'),
    path('<int:pk>/', views.get_post_detail, name='post_detail'),
    path('category/<int:pk>/', views.get_category, name='category')
]
