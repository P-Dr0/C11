distancia = float(input('Digite a distância da viagem em Km: '))

if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45

print(f'O preço da passagem é: R${preco:.2f}')


numero = int(input('Digite um número entre 1000 e 9999: '))

unidade = numero % 10
dezena = (numero // 10) % 10
centena = (numero // 100) % 10
milhar = (numero // 1000) % 10

print(f'Unidade: {unidade}')
print(f'Dezena: {dezena}')
print(f'Centena: {centena}')
print(f'Milhar: {milhar}')


import math

numero = float(input('Digite um número decimal: '))

raiz = math.sqrt(numero)
teto = math.ceil(numero)
chao = math.floor(numero)
parte_inteira = int(numero)

print(f'Raiz quadrada: {raiz:.2f}')
print(f'Função teto: {teto}')
print(f'Função chão: {chao}')
print(f'Parte inteira: {parte_inteira}')


