import os
import django
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'unifood.settings')
django.setup()

from products.models import Vendedor, Setor, Produto

NOME_VENDEDORES = ["João", "Maria", "Pedro", "Ana", "Lucas"]
CATEGORIAS_PRODUTOS = ["Lanche", "Bebida", "Sobremesa"]
DESCRICOES_PRODUTOS = ["Delicioso lanche caseiro", "Refrescante refrigerante", "Doce tentação"]

def criar_setores():
    setores = ["Alimentos", "Bebidas", "Doces", "Fast-Food"]

    for nome in setores:
        Setor.objects.get_or_create(nome=nome)
    print('Setores criados com sucesso.')

def criar_vendedores():
    for nome in NOME_VENDEDORES:
        vendedor, created = Vendedor.objects.get_or_create(nome=nome, email=f'{nome.lower()}@exemplo.com', telefone='(00) 0000-0000')
        setores = Setor.objects.all()
        setores_aleatorios = random.sample(list(setores), random.randint(1, len(setores)//2))
        vendedor.setores.set(setores_aleatorios)
        vendedor.save()
    print('Vendedores criados com sucesso.')

def criar_produtos():
    vendedores = Vendedor.objects.all()

    for i in range(10):  # Cria 10 produtos
        nome = f"Produto {i+1}"
        preco = random.uniform(5, 15)
        categoria = random.choice(CATEGORIAS_PRODUTOS)
        vendedor = random.choice(vendedores)
        descricao = random.choice(DESCRICOES_PRODUTOS)

        Produto.objects.get_or_create(nome=nome, preco=preco, categoria=categoria, vendedor=vendedor, descricao=descricao)
    print('Produtos criados com sucesso.')

def criar_dados_ficticios():
    criar_setores()
    criar_vendedores()
    criar_produtos()

if __name__ == '__main__':
    criar_dados_ficticios()
