from django.db import models


class BannerModel(models.Model):
    image = models.ImageField(upload_to='home_banners')
    title = models.CharField(max_length=16)
    sub_title = models.CharField(max_length=32)
    description = models.TextField()
    video_link = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class AboutModel(models.Model):
    image = models.ImageField(upload_to='home_about')
    title = models.CharField(max_length=64)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
