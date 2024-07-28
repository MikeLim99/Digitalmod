from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()

    def __str__(self):
        return self.title + ' | ' + str(self.author)
    
class Portfolio(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    image = models.FileField(blank=True)
    link = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title
    
class PortfolioGallery(models.Model):
    portfolio = models.ForeignKey(Portfolio, related_name= 'img', on_delete=models.CASCADE, null=True, blank=True)
    images = models.ImageField(upload_to='Portfolio/ImageGallery/')

class Services(models.Model):
    title = models.CharField(max_length=50)
    icon_code = models.CharField(max_length=255, null=True,blank=True)
    description = models.TextField()

    def __str__(self):
        return self.title