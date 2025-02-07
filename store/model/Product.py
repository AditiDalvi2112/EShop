from django.db import models
from .category import Category

class Product(models.Model):
    objects = None
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=300, default='', null=True, blank=True)  # Changed max_length
    image = models.ImageField(upload_to='uploads/products/')

    @staticmethod
    def get_products_by_id(ids):
        return Product.objects.filter(id__in=ids)

    @staticmethod
    def get_all_products() -> object:
        return Product.objects.all()

    @staticmethod
    def get_all_products_by_categoryid(Category_id):
        if Category_id:
             return Product.objects.filter(category=Category_id)
        else:
            return Product.get_all_products()

