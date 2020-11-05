from django.db import models

# Create your models here.
from django.urls import reverse


class Category(models.Model):
    title = models.CharField(default='Новинки', max_length=100, verbose_name='Категория')
    slug = models.SlugField(max_length=100, verbose_name='Url', unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category', kwargs={"slug": self.slug})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']


class Genre(models.Model):
    title = models.CharField(default='Юмор', max_length=50, verbose_name='Жанр')
    slug = models.SlugField(max_length=50, verbose_name='Url', unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('genre', kwargs={"slug": self.slug})

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'
        ordering = ['title']


class Town(models.Model):
    title = models.CharField(max_length=100, verbose_name='Город')
    slug = models.SlugField(max_length=100, verbose_name='Url', unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'
        ordering = ['title']


class Type(models.Model):
    title = models.CharField(max_length=100, verbose_name='Предложение')
    slug = models.SlugField(max_length=100, verbose_name='Url', unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Вариант'
        verbose_name_plural = 'Варианты'
        ordering = ['title']


class Owner(models.Model):
    name = models.CharField(max_length=100, verbose_name='Владелец книги')
    slug = models.SlugField(max_length=100, verbose_name='Url', unique=True)
    email = models.EmailField(blank=False, primary_key=True, unique=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Владелец'
        verbose_name_plural = 'Владельцы'
        ordering = ['name']

    def get_absolute_url(self):
        return reverse('owner', kwargs={"slug": self.slug})


class Book(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название книги')
    slug = models.SlugField(max_length=100, verbose_name='Url', unique=True)
    author = models.CharField(max_length=100, verbose_name='Автор книги')
    content = models.TextField(blank=True, verbose_name='Аннотация')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Опубликовано')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    views = models.IntegerField(default=0, verbose_name='Кол-во просмотров')
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name='books', verbose_name='Владелец книги')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='books', verbose_name='Раздел')
    genres = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name='books', verbose_name='Жанры')
    town = models.ForeignKey(Town, on_delete=models.CASCADE, related_name='books', verbose_name='Город')
    type = models.ForeignKey(Type, on_delete=models.CASCADE, related_name='books', verbose_name='Предложение')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
        ordering = ['-created_at']
        permissions = (("can_post", "can post"),)

    def get_absolute_url(self):
        return reverse('book', kwargs={"slug": self.slug})


# создаем новый класс для комментариев
class Comment(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.book)
