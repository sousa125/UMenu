from django.shortcuts import render, get_object_or_404
from products.models import Produto, Vendedor, Setor
from django.shortcuts import render

def buscar_vendedores(request):
    setor_id = request.GET.get('setor_id')
    vendedores = Vendedor.objects.filter(setores__id=setor_id)
    return render(request, 'vendedores.html', {'vendedores': vendedores})

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