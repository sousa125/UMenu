from django.shortcuts import render, get_object_or_404
from products.models import Produto, Vendedor, Setor

def lista_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'lista_produtos.html', {'produtos': produtos})

def detalhes_produto(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    return render(request, 'detalhes_produto.html', {'produto': produto})

def home(request):
    setores = Setor.objects.all()  # Obtém todos os setores do banco de dados
    vendedores = Vendedor.objects.all()  # Obtém todos os vendedores do banco de dados

    context = {
        'setores': setores,
        'vendedores': vendedores
    }

    return render(request, 'home.html', context)