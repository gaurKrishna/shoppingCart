from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Product(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(blank=False)
    genre = models.CharField(max_length=150, default=None)
    price = models.FloatField(default = None)
    review_stars = models.CharField(max_length=1)
    sample_picture1 = models.FileField(blank=True)
    sample_picture2 = models.FileField(blank=True)
    sample_picture3 = models.FileField(blank=True)

    def get_absolute_url(self):
       return reverse('home:homepage')

    def __str__(self):
       return self.title

class Cart(models.Model):
   Cart_owner = models.ForeignKey(User, on_delete=models.CASCADE)
   Cart_content = models.ForeignKey(Product, on_delete=models.CASCADE)
   Number_of_products = models.IntegerField(default=1)

   def get_absolute_url(self):
      return reverse('home:Cart_details', kwargs={'pk': self.pk})

   def __str__(self):
      return self.Cart_owner.username+ '-' + self.Cart_content.title
