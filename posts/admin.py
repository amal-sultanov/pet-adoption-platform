from django.contrib import admin

from .models import PostCategoryModel, PostModel

admin.site.register(PostCategoryModel)
admin.site.register(PostModel)
