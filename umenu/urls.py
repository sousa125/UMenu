from django.contrib import admin
from django.urls import path
from products import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('produtos/', views.lista_produtos, name='lista_produtos'),
    path('produtos/<int:produto_id>/', views.detalhes_produto, name='detalhes_produto'),
    path('buscar-vendedores/', views.buscar_vendedores, name='buscar_vendedores'),
    path('catalogo/<int:vendedor_id>/', views.catalogo_vendedor, name='catalogo_vendedor'),
]
