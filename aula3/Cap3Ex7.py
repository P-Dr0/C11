#EX7

ingredientes_receita = {'farinha', 'açúcar', 'ovos', 'fermento', 'leite'}

ingredientes_pessoa1 = {'farinha', 'ovos', 'leite'}
ingredientes_pessoa2 = {'açúcar', 'ovos', 'manteiga'}

faltam_pessoa1 = ingredientes_receita - ingredientes_pessoa1
faltam_pessoa2 = ingredientes_receita - ingredientes_pessoa2

print(f'Ingredientes que a pessoa 1 ainda precisa comprar: {faltam_pessoa1}')
print(f'Ingredientes que a pessoa 2 ainda precisa comprar: {faltam_pessoa2}')