from django.db import models
from django.contrib.auth.models import AbstractUser
import re

# Custom User model
class User(AbstractUser):
    pass  # Add any custom fields if needed

# Article model
from django.utils.text import slugify

class Articles(models.Model):
    article_id = models.AutoField(primary_key=True)  # Auto-incrementing primary key
    slug = models.CharField(max_length=255, unique=True, blank=True)  # Unique string identifier
    
    category = models.ForeignKey('main.Categories', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    headline_image = models.ImageField(upload_to='media/images/headline_images/', blank=True, null=True)
    author = models.ForeignKey('main.User', on_delete=models.CASCADE)
   
    view_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        base_slug =  re.sub(r'\s+', '-', self.slug)
        slug = base_slug
        counter = 1
        while Articles.objects.filter(slug=slug).exists():
               if(Articles.objects.get(slug=slug).article_id==self.article_id):
                 pass
                 break
               else: 
                slug = f"{base_slug}-{counter}"
                counter += 1
        self.slug = slug
        super().save(*args, **kwargs)
    def __str__(self):
        return self.slug
class View(models.Model):
    view_id = models.AutoField(primary_key=True)
    view_name = models.CharField(max_length=255)
    content = models.TextField()
    view_heading = models.CharField(max_length=255)
    article = models.ForeignKey(Articles, on_delete=models.CASCADE)
    polled_votes = models.IntegerField(default=0)
    def __str__(self):
        return self.view_heading
from django.db import models
from django.contrib.auth.models import User  # Assuming you're using the default User model

class ArticleView(models.Model):
    article = models.ForeignKey('Articles', on_delete=models.CASCADE)  
    viewed_at = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return f"Article{self.article.title} at {self.viewed_at}"

class Categories(models.Model):
    category = models.CharField(max_length=255, primary_key=True)

    def __str__(self):
        return self.category


