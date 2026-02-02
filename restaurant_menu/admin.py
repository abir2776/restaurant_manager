from django.contrib import admin

from restaurant_menu.models import Category, Image, OpeningHours, Product, Tag

admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Product)
admin.site.register(Image)
admin.site.register(OpeningHours)
