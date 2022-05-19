import imp
from django.contrib import admin
from platform_api.models import Color, Supplier, Brand, Product

# Register your models here.
admin.site.register(Color)
admin.site.register(Supplier)
admin.site.register(Brand)
admin.site.register(Product)