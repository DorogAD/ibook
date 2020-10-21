from django.db import models

# Create your models here.
from django.urls import reverse

'''
Category
=========
title, slug

Genre
=========
title, slug

Book
=========
title, slug, author, owner, content, created_at, photo, views, category, genre, comment, town, type
'''
'''
from django.db import models
from django_ckeditor_5.fields import CKEditor5Field


class Article(models.Model):
    title=models.CharField('Title', max_length=200)
    text=CKEditor5Field('Text', config_name='extends')
#?
'''

class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name='Категория')
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
    title = models.CharField(max_length=50, verbose_name='Жанр')
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



class Book(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название книги')
    slug = models.SlugField(max_length=100, verbose_name='Url', unique=True)
    author = models.CharField(max_length=100, verbose_name='Автор книги')
    content = models.TextField(blank=True, verbose_name='Аннотация')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Опубликовано')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    views = models.IntegerField(default=0, verbose_name='Кол-во просмотров')
    owner = models.CharField(max_length=100, verbose_name='Владелец книги')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='books', verbose_name='Раздел')
    genres = models.ManyToManyField(Genre, blank=True, related_name='books', verbose_name='Жанры')
    town = models.ForeignKey(Town, on_delete=models.PROTECT, related_name='books', verbose_name='Город')
    type = models.ForeignKey(Type, on_delete=models.PROTECT, related_name='books', verbose_name='Предложение')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
        ordering = ['-created_at']

    def get_absolute_url(self):
        return reverse('book', kwargs={"slug": self.slug})


class Owner(models.Model):
    name = models.ForeignKey(Book, on_delete=models.PROTECT, related_name='books', verbose_name='Владелец')
    slug = models.SlugField(max_length=100, verbose_name='Url', unique=True)
    email = models.EmailField(blank=False, primary_key=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Владелец'
        verbose_name_plural = 'Владельцы'
        ordering = ['name']

    def get_absolute_url(self):
        return reverse('owner', kwargs={"slug": self.slug})