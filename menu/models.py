from django.db import models
from category.models import Category
from django.contrib.auth import get_user_model

User = get_user_model() 

class Menu(models.Model):
    STATUS_CHOICES =(('in_stock', 'Доступен к заказу'), 
                     ('out_stock', 'Стоп-лист'))
    title = models.CharField(max_length=255, unique=True)
    description = models.CharField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='menu')
    preview = models.ImageField(upload_to='images/', null=True)
    price = models.DecimalField(max_digits=9, decimal_places=2, null=True)
    stock = models.CharField(max_length=50, choices=STATUS_CHOICES)
    owner = models.ForeignKey(User, related_name='menu', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}'
    
    class Meta:
        verbose_name = 'Позиция'
        verbose_name_plural = 'Позиции'

class MenuImages(models.Model):
    title = models.CharField(max_length=100, blank=True)
    images = models.ImageField(upload_to='images/')
    post = models.ForeignKey('Menu', related_name='images', on_delete=models.CASCADE)

    def generate_name(self):
        from random import randint
        return 'images' + str(randint(100_000, 1000_000))
    
    def save(self, *args, **kwargs):
        self.title = self.generate_name()
        return super(MenuImages, self).save(*args, **kwargs)