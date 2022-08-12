from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField
# Create your models here.
    
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


class Solar(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    image = models.ImageField(blank=True)
    date = models.DateField(auto_now_add=True)
    name = models.CharField(max_length=100)
    content = models.CharField(max_length=200)
    tags =  models.CharField(max_length=100)
    image1 = models.ImageField(blank=True)
    image2 = models.ImageField(blank=True)
    image3 = models.ImageField(blank=True)
    image4 = models.ImageField(blank=True)
    image5 = models.ImageField(blank=True)
    body = RichTextField()


    class Meta:
        ordering = ['-date']
        get_latest_by = 'date'

    def __str__(self):
        return self.title
        
    def get_absolute_url(self):
        return reverse('project_details',kwargs={'slug':self.slug})


class Featured(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)
    pics = models.ImageField(blank=True)
    
    class Meta:
        ordering = ['-date']
        get_latest_by = 'date'

    def __str__(self):
        return self.title