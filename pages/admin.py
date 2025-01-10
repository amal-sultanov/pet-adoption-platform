from django.contrib import admin

from .models import BannerModel, AboutModel

admin.site.register(BannerModel)
admin.site.register(AboutModel)
