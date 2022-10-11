from django.db import models
from django.urls import reverse


class CategoryModel(models.Model):
    title = models.CharField(max_length=50, db_index=True)
    slug = models.SlugField(max_length=50)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('CategoryPage', kwargs={'cat_id': self.pk})


class ArticleModel(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=50, unique=True)
    content = models.TextField()
    photo = models.ImageField(upload_to="photos", blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    author = models.CharField(max_length=30, null=True)
    category = models.ForeignKey(CategoryModel, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('ArticlePage', kwargs={'post_id': self.pk})
