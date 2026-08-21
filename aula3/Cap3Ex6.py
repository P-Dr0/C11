#EX6

ingredientes = ['farinha', 'açúcar', 'ovos', 'fermento', 'leite']

ingredientes.append('manteiga')
print(f'Após adicionar no final: {ingredientes}')

ingredientes.insert(2, 'baunilha')
print(f'Após inserir na posição 2: {ingredientes}')

ingredientes.remove('fermento')
print(f'Após remover "fermento": {ingredientes}')