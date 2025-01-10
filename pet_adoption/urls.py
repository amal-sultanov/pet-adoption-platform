from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('users.urls', namespace='users')),
    path('pets/', include('pets.urls', namespace='pets')),
    path('posts/', include('posts.urls', namespace='posts')),
    path('', include('pages.urls', namespace='pages'))
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
