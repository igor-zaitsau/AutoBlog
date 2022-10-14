from django.db import models
from django.urls import reverse


class CategoryModel(models.Model):
    title = models.CharField(max_length=50, db_index=True, verbose_name='Название')
    slug = models.SlugField(max_length=50, unique=True, verbose_name='URL')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('CategoryPage', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class ArticleModel(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Название')
    slug = models.SlugField(max_length=50, unique=True, verbose_name='URL')
    content = models.TextField(verbose_name='Статья')
    photo = models.ImageField(upload_to="photos", blank=True, verbose_name='Фото')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Дата публикации')
    is_published = models.BooleanField(default=True, verbose_name='Публикация')
    author = models.CharField(max_length=30, verbose_name='Автор')
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE, verbose_name='Категория')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('ArticlePage', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'