import imp
from django.contrib import admin
from platform_api.models import Cores, Fornecedor, Marca, Produto

# Register your models here.
admin.site.register(Cores)
admin.site.register(Fornecedor)
admin.site.register(Marca)
admin.site.register(Produto)