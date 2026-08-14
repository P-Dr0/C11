nome_completo = input('Digite seu nome completo: ')

print(nome_completo.upper())
print(nome_completo.lower())
print(len(nome_completo))

partes = nome_completo.split()
partes[-1] = 'do Inatel'
novo_nome = ' '.join(partes)
print(novo_nome)
