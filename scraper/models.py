from django.db import models

# Create your models here.
    
    
    
class News(models.Model):
    CATEGORY_CHOICES = [
        ('sports', 'Sports'),
        ('national', 'National'),
        ('world', 'World'),
        ('entertainment', 'Entertainment'),
        ('politics', 'Politics'),
        ('economy', 'Economy'),
        ('arts', 'Arts'),
        ('others', 'Others'),
    ]
    title = models.CharField(max_length=255)
    img_src = models.URLField(max_length=255)
    url = models.URLField(max_length=255)
    category = models.CharField(max_length=255, choices=CATEGORY_CHOICES)
    def __str__(self):
        return self.title
    

