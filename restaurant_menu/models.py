from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=255)
    image = models.FileField(upload_to="category", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Image(models.Model):
    image = models.FileField(upload_to="products")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return super().__str__()


class Product(models.Model):
    STATUS_CHOICES = [("active", "Active"), ("inactive", "Inactive")]
    title = models.CharField(max_length=255)
    category = models.ManyToManyField(Category, null=True, blank=True)
    images = models.ManyToManyField(
        Image, related_name="products", null=True, blank=True
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=500)
    tags = models.ManyToManyField(Tag, null=True, blank=True)
    is_popular = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="active")

    def __str__(self):
        return self.title


class OpeningHours(models.Model):
    day = models.CharField()
    start_time = models.TimeField()
    end_time = models.TimeField()
