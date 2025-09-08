from django.db import models

class Service(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='services/')

    def __str__(self):
        return self.title




class Laptop(models.Model):
    name = models.CharField(max_length=200)
    specs = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to="laptops/")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Accessory(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to="accessories/")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name