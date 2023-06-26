from django.db import models
from PIL import Image
from django.core.files import File
from io import BytesIO
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField()
    
    class Meta:
        verbose_name_plural = 'Категории'
        ordering = ('name',)
        
    def __str__(self):
        return self.name



class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    slug = models.SlugField()
    description = models.TextField(max_length=300, null=True, blank=True)
    price = models.IntegerField()
    created_at = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='uploads/', blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Товары'
        ordering = ('-created_at',)
        
    def __str__(self):
        return self.name
    
    def get_thumbnail(self):
        if self.thumbnail:
            return self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()
                
                return self.thumbnail.url
            else:
                return 'https://via.placeholder.com/240x240x.jpg'
            
    def make_thumbnail(self, image, size=(300,300)):
        img = Image.open(image)
        img = img.convert('RGB')
        img.thumbnail(size)
        
        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)
        
        thumbnail = File(thumb_io, name=image.name)
        
        return thumbnail
    
    def get_rating(self):
        reviews_total = 0

        for review in self.reviews.all():
            reviews_total += review.rating

        if reviews_total > 0:
            return reviews_total / self.reviews.count()
        
        return 0
    
class Review(models.Model):
    product = models.ForeignKey(Product, related_name='reviews', on_delete=models.CASCADE)
    rating = models.IntegerField()
    content = models.CharField(max_length=250)

    created_by = models.ForeignKey(User, related_name='reviews', on_delete=models.CASCADE)
    created_at = created_at = models.DateField(auto_now_add=True)


