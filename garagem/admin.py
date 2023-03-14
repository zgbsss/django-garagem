from django.contrib import admin

from .models import Marca
admin.site.register(Marca)

from .models import Categoria
admin.site.register(Categoria)