import os
from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True, db_index=True)
    
    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category:ProductListByCategory', args=[self.slug])
"""    
def get_upload_path(instanse, filename):
    filename = instanse.slug + '.' + filename.split('.')[1]
    return os.path.join('images/', filename)
"""

class Product(models.Model):
    category = models.ForeignKey(Category , related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=150, db_index=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    createdDate = models.DateTimeField(auto_now_add=True, verbose_name='Data dodania')
    upgradeDate = models.DateTimeField(auto_now=True, verbose_name='Data aktualizacji')
    images = models.ImageField(upload_to='images/', blank='True', )

    class Meta:
        ordering = ['name']
        index_together = [('id', 'slug'),]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category:ProductDetails', args=[ self.id, self.slug])
