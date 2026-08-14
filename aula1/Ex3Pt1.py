palavra = input('Digite uma palavra: ')

vogais = 0
tem_a = False

for letra in palavra:
    print(letra.upper())
    if letra.lower() in 'aeiou':
        vogais += 1
    if letra.upper() == 'A':
        tem_a = True

print('Quantidade de vogais:', vogais)
print('A letra A está presente:', tem_a)