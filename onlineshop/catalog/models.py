from sre_parse import Verbose
from tabnanny import verbose
from unicodedata import name
from urllib import request
from django.db import models
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# All goods
class Goods(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(blank=True, verbose_name='Описание')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name='Фото')
    slug = models.SlugField(max_length=100, verbose_name='URL')
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория')
    price = models.IntegerField(verbose_name='Цена')

    def __str__(self):
        return self.name

    class Meta():
        verbose_name = 'Товары'
        verbose_name_plural = 'Товары'
        ordering = ['id']

# Categories
class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Категория')
    slug = models.SlugField(max_length=100, unique=True, verbose_name='URL')

    def __str__(self):
         return self.name

    #def get_absolute_url(self):
    #    return reverse('goods:category', kwargs={'cat_slug' : self.slug})

    class Meta():
        verbose_name = 'Категории'
        verbose_name_plural = 'Категории'
        ordering = ['id']

# Feedbacks
class Feedbacks(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    feedback_text = models.TextField(max_length=255, verbose_name='Текст')
    ratingcomment = models.IntegerField(verbose_name='Рейтинг')
    date = models.DateField(auto_now=True, verbose_name='Дата')
    date_time = models.DateTimeField(auto_now=True, verbose_name='Дата-Время')

    def __str__(self):
         return self.name

    class Meta():
        verbose_name_plural = 'отзывы'
        verbose_name = 'отзывы'
        ordering = ['id']

# user profile
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Заказчик')
    username = models.CharField(max_length=50, verbose_name='Имя(id заказчика)')

    def __str__(self):
        return self.username

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    class Meta():
        verbose_name_plural = 'Пользователи(доп. информация)'
        verbose_name = 'Пользователи(доп. информация)'
        ordering = ['id']

# user orders
class Orders(models.Model):
    order_number = models.IntegerField(verbose_name='Номер заказа')
    owner = models.CharField(max_length=50, blank=True, verbose_name='Заказчик(Username)')
    items_ordered = models.CharField(max_length=200, blank=True, verbose_name='id`s товаров')
    order_owner = models.ForeignKey('Profile', on_delete=models.PROTECT, verbose_name='Заказчик(id)')
    total_price = models.IntegerField(verbose_name='Конечная стоимость товаров', blank=True)

    def __str__(self):
        return str(self.order_number)

    class Meta():
        verbose_name_plural = 'Заказы'
        verbose_name = 'Заказы'
        ordering = ['id']


# class Goods(models.Model):
#     name = models.TextField(verbose_name='Название')
#     description = models.TextField(verbose_name='Описание')
#     photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото')
#     slug = models.SlugField(verbose_name='URL')
#     cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория')
#     price = models.IntegerField(verbose_name='Цена')

#     def __str__(self):
#         return self.name

#     class Meta():
#         verbose_name = 'Товары'
#         verbose_name_plural = 'Товары'
#         ordering = ['id']

# # Categories
# class Category(models.Model):
#     name = models.TextField(verbose_name='Категория')
#     slug = models.SlugField(unique=True, verbose_name='URL')

#     def __str__(self):
#          return self.name

#     #def get_absolute_url(self):
#     #    return reverse('goods:category', kwargs={'cat_slug' : self.slug})

#     class Meta():
#         verbose_name = 'Категории'
#         verbose_name_plural = 'Категории'
#         ordering = ['id']

# # Feedbacks
# class Feedbacks(models.Model):
#     name = models.TextField(verbose_name='Имя')
#     feedback_text = models.TextField(verbose_name='Текст')
#     ratingcomment = models.IntegerField(verbose_name='Рейтинг')
#     date = models.DateField(auto_now=True, verbose_name='Дата')
#     date_time = models.DateTimeField(auto_now=True, verbose_name='Дата-Время')

#     def __str__(self):
#          return self.name

#     class Meta():
#         verbose_name_plural = 'отзывы'
#         verbose_name = 'отзывы'
#         ordering = ['id']

# # user profile
# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Заказчик')
#     username = models.TextField(verbose_name='Имя(id заказчика)')

#     def __str__(self):
#         return self.username

#     @receiver(post_save, sender=User)
#     def create_user_profile(sender, instance, created, **kwargs):
#         if created:
#             Profile.objects.create(user=instance)

#     @receiver(post_save, sender=User)
#     def save_user_profile(sender, instance, **kwargs):
#         instance.profile.save()

#     class Meta():
#         verbose_name_plural = 'Пользователи(доп. информация)'
#         verbose_name = 'Пользователи(доп. информация)'
#         ordering = ['id']

# # user orders
# class Orders(models.Model):
#     order_number = models.IntegerField(verbose_name='Номер заказа')
#     owner = models.TextField(verbose_name='Заказчик(Username)')
#     items_ordered = models.TextField(verbose_name='id`s товаров')
#     order_owner = models.ForeignKey('Profile', on_delete=models.PROTECT, verbose_name='Заказчик(id)')
#     total_price = models.IntegerField(verbose_name='Конечная стоимость товаров')

#     def __str__(self):
#         return str(self.order_number)

#     class Meta():
#         verbose_name_plural = 'Заказы'
#         verbose_name = 'Заказы'
#         ordering = ['id']