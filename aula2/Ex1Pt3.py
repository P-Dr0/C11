sexo = input('Digite seu sexo (M/F): ')

while sexo != 'M' and sexo != 'F':
    sexo = input('Valor inválido! Digite M ou F: ')

if sexo == 'M':
    print('Você é homem')
else:
    print('Você é mulher')