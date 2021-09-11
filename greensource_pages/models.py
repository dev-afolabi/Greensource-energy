from django.db import models
from django.urls import reverse

# Create your models here.

class Galllery(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(blank=True)
    date = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-date']
        get_latest_by = 'date'

    def __str__(self):
        return self.title


    

class Images(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)
    thumb = models.ImageField(blank=True)
    
    class Meta:
        ordering = ['-date']
        get_latest_by = 'date'

    def __str__(self):
        return self.title


class Testimonial(models.Model):
    name = models.CharField(max_length = 200)
    title = models.CharField(max_length=100)
    image = models.ImageField(blank=True)
    date = models.DateField(auto_now_add=True)
    body = models.TextField()

    class Meta:
        ordering = ['-date']
        get_latest_by = 'date'

    def __str__(self):
        return self.title



