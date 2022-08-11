from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()

    def __str__(self):
        return self.title

class Post(models.Model):
    title = models.CharField(max_length=100)
    short_description = models.CharField(max_length=300)
    slug = models.SlugField(unique=True)
    body = models.TextField()
    thumb = models.ImageField(blank=True, )
    date = models.DateField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-date']
        get_latest_by = 'date'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article_detail',kwargs={'slug':self.slug})

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE, related_name = 'comments')
    name = models.CharField(max_length = 200)
    email = models.EmailField(blank = True)
    date = models.DateField(auto_now_add=True)
    content = models.TextField()
    class Meta:
        ordering = ['-date']
        get_latest_by = 'date'
    def __str__(self):
            return 'Comment {} by {}'.format(self.content,self.name)