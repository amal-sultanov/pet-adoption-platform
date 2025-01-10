from django.db import models


class PostCategoryModel(models.Model):
    title = models.CharField(max_length=64)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class PostModel(models.Model):
    image = models.ImageField(upload_to='posts')
    title = models.CharField(max_length=64)
    description = models.TextField()
    category = models.ForeignKey(PostCategoryModel, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
