from django.db import models

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=255)
    img_src = models.CharField(max_length=255)
    url = models.URLField(max_length=255)

    def __str__(self):
        return self.title
    


class Site(models.Model):
    name = models.CharField(max_length=255)
    url = models.URLField(max_length=255)
    
    def __str__(self):
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length=255)
    site = models.ForeignKey(Site, on_delete=models.CASCADE, related_name='site')
    
    def __str__(self):
        return self.name