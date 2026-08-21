#EX1

classificacao = ('Flamengo','Barcelona','Real Madrid','Pouso Alegre','Remo')
print(f'3 primeiros colocados: {classificacao[:3]}')
print(f'Ultimos 2 colocados: {classificacao[3:]}')
print(f'Times em ordem alfabetica: {sorted(classificacao)}')
print(f'Posição do Barcelona: {classificacao.index("Barcelona")}')

print(' ')


#EX2

loja1 = {'Iphone 15', 'Galaxy S24', 'Xiaomi 14', 'Moto G84'}
loja2 = {'Galaxy S24', 'Xiaomi 14', 'Pixel 8', 'Iphone 14'}
total_modelos = loja1 | loja2
print(f'Modelos no total (opção de comprar visitando as duas): {total_modelos}')
modelos_ambas = loja1 & loja2
print(f'Modelos disponíveis em ambas as lojas: {modelos_ambas}')

print(' ')


#EX3

nome = input('Digite o nome do aluno: ')
media = float(input('Digite a média do aluno: '))

if media >= 50:
    situacao = 'AP'
else:
    situacao = 'RP'

aluno = {'nome': nome, 'media': media, 'situacao': situacao}

print(aluno)