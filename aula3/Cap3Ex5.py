#EX5

n = int(input('Numro de pessoas: '))
idades = []
mulheresmenores = 0

for c in range(n):
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = input('Sexo: ')

    idades.append(idade)

    if sexo == 'F' and idade < 20:
        mulheresmenores += 1

media = sum(idades) / len(idades)

print(f'Media de idade: {media}')
print(f'Quantidade de mulheres menores de 20: {mulheresmenores}')