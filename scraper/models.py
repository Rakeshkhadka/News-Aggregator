from django.db import models

# Create your models here.
    
    
    
class News(models.Model):
    CATEGORY_CHOICES = [
        ('sports', 'Sports'),
        ('video', 'Video'),
        ('national', 'National'),
        ('world', 'World'),
        ('entertainment', 'Entertainment'),
    ]
    title = models.CharField(max_length=255)
    img_src = models.URLField(max_length=255)
    url = models.URLField(max_length=255)
    category = models.CharField(max_length=255, choices=CATEGORY_CHOICES)
    def __str__(self):
        return self.title