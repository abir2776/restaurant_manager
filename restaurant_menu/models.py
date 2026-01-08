from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=255)
    image = models.FileField(upload_to="category", null=True, blank=True)

    def __str__(self):
        return super().__str__()


class FoodCategory(models.Model):
    title = models.CharField(max_length=255)
    image = models.FileField(upload_to="category", null=True, blank=True)

    def __str__(self):
        return super().__str__()


class Tag(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return super().__str__()


class Image(models.Model):
    image = models.FileField(upload_to="products")

    def __str__(self):
        return super().__str__()


class Product(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    food_category = models.ForeignKey(FoodCategory, on_delete=models.CASCADE)
    images = models.ManyToManyField(Image, related_name="products")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=500)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return super().__str__()
