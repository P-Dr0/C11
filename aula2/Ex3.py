palavra = input('Digite uma palavra: ')

vogais = 'AEIOU'
contador_vogais = 0
tem_letra_a = False

for letra in palavra:
    letra_maiuscula = letra.upper()
    print(letra_maiuscula)
    if letra_maiuscula in vogais:
        contador_vogais += 1
    if letra_maiuscula == 'A':
        tem_letra_a = True

print(f'Quantidade de vogais: {contador_vogais}')
print(f'A letra A está presente: {tem_letra_a}')


num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))

adicao = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2
divisao = num1 / num2
resto = num1 % num2
potencia = num1 ** num2

print(f'Adição: {adicao}')
print(f'Subtração: {subtracao}')
print(f'Multiplicação: {multiplicacao}')
print(f'Divisão: {divisao:.2f}')
print(f'Resto da divisão: {resto}')
print(f'Potência: {potencia}')