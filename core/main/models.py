from tabnanny import verbose
from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField('Category name', max_length=30)
    img = models.ImageField('Category image', upload_to='media', null=True)
    about = models.TextField('Category about', null=True)
    price = models.FloatField('Category price', null=True)
    

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

class Users(models.Model):
    username = models.CharField('User name', max_length=30)
    img = models.ImageField('User image', upload_to='media', null=True)


    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Username'
        verbose_name_plural = 'Usernames'





