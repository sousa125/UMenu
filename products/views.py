from django.shortcuts import render, get_object_or_404
from products.models import Produto, Vendedor, Setor
from django.shortcuts import render
import json

def buscar_vendedores(request):
    setor_id = request.GET.get('setor_id')
    search_term = request.GET.get('search_term')

    vendedores = Vendedor.objects.filter(setores__id=setor_id)

    if search_term:
        vendedores = vendedores.filter(nome__icontains=search_term)

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

def catalogo_vendedor(request, vendedor_id):
    produtos = Produto.objects.filter(vendedor=vendedor_id)
    vendedor = Vendedor.objects.get(id=vendedor_id)
    context = {
        'produtos': produtos,
        'vendedor': vendedor,
    }
    return render(request, 'catalogo.html', context)


from django.shortcuts import render

from django.shortcuts import render

def carrinho(request):
    produtos = []
    for key, value in request.GET.items():
        if key.startswith('produtos') and value != '':
            split_key = key.split('.')
            index = int(''.join(filter(str.isdigit, split_key[0])))
            attr = split_key[1]
            if len(produtos) <= index:
                produtos.append({})
            produtos[index][attr] = value
    # Consulta os detalhes dos produtos no banco de dados (isso depende do seu modelo de dados)
    # Supondo que você tenha um modelo chamado 'Produto' com os campos 'nome' e 'quantidade'
    product_ids = [produto['id'] for produto in produtos]
    products = Produto.objects.filter(id__in=product_ids)
    # Anexa a quantidade a cada produto com base nos dados do carrinho
    produtos_com_quantidade = []
    vendedor = Vendedor.objects.get(id=products[0].vendedor_id)
    print(vendedor.telefone)
    for produto in products:
        index = product_ids.index(str(produto.id))
        quantidade = int(produtos[index]['quantidade'])
        produtos_com_quantidade.append({'produto': produto, 'quantidade': quantidade})
    
    context = {'produtos': produtos_com_quantidade, 'vendedor_telefone':vendedor.telefone }
    return render(request, 'carrinho.html', context)
