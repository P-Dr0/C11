#EX8

produtos = []

for i in range(3):
    nome = input('Nome do produto: ')
    preco = float(input('Preço do produto: '))
    quantidade = int(input('Quantidade em estoque: '))

    produto = {
        'nome': nome,
        'preco': preco,
        'quantidade': quantidade
    }

    produtos.append(produto)

for produto in produtos:
    valor_total = produto['preco'] * produto['quantidade']
    print(f"Produto: {produto['nome']}, Valor total em estoque: R${valor_total:.2f}")