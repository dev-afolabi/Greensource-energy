from django.db import models

# Create your models here.

class Galllery(models.Model):
    title = models.CharField(max_length=50)
    heading_id = models.CharField(max_length=20, blank=True)
    description = models.CharField(max_length=200)
    date = models.DateField(auto_now_add=True)
    image = models.ImageField(blank=True)
    second_image = models.ImageField(blank=True)
    
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



