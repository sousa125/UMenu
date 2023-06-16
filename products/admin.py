from django.contrib import admin
from .models import Vendedor, Setor, Produto

admin.site.register(Vendedor)
admin.site.register(Setor)
admin.site.register(Produto)
