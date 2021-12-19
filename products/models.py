from django.db import models


class Category(models.Model):
    name = models.CharField(unique=True, max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Product(models.Model):

    STATUS_CHOICES = [
        ('in_stock', 'In stock'),
        ('out_of_stock', 'Out of stock')
    ]

    name = models.CharField(unique=True, max_length=255)
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE,
                                 related_name='product')
    price = models.DecimalField(decimal_places=2, max_digits=10)
    status = models.CharField(choices=STATUS_CHOICES, max_length=255)
    remains = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

