#EX4

pessoas = {}

for c in range(3):
    nome = input('Digite o nome:')
    peso = float(input('Digite o peso:'))
    pessoas[nome] = peso

maispesada = max(pessoas, key=pessoas.get)
maisleve = min(pessoas, key=pessoas.get)

print(f'Pessoa mais pesada: {maispesada}')
print(f'Pessoa mais leve: {maisleve}')

