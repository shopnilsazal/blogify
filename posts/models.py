from django.db import models
from django.utils.text import slugify

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
    image = models.FileField(null=True, blank=True, upload_to='%Y/%m')
    content = models.TextField()
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    categories = models.ManyToManyField("Category")
    tags = models.ManyToManyField("Tag")

    def __str__(self):
        return self.title

    def list_categories(self):
        return ", ".join([category.name for category in self.categories.all()])

    def list_tags(self):
        return ", ".join([tag.name for tag in self.tags.all()])


class Category(models.Model):
    name = models.CharField(max_length=70)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=70)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name
