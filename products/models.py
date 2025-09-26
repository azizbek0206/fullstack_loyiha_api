from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    description = models.TextField(blank=True, default='')
    sold = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Order(models.Model):
    buyer = models.CharField(max_length=255)
    products = models.TextField()
    total = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50, choices=[
        ('yangi', 'Yangi'),
        ('tolanmoqda', 'To\'lanmoqda'),
        ('yetkazildi', 'Yetkazildi'),
        ('bekor', 'Bekor qilindi')
    ])
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} - {self.buyer}"

class User(models.Model):
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=50, choices=[
        ('admin', 'Admin'),
        ('sotuvchi', 'Sotuvchi'),
        ('xaridor', 'Xaridor')
    ])
    email = models.EmailField(unique=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name