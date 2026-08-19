import numpy as np

dataset = np.loadtxt('/Users/pedrohenriquedossantosaraujo/PycharmProjects/C11/C11Aulas/aula4pt2/space.csv',delimiter=';', dtype='str', encoding='utf-8')

id = dataset[1:,0]
company = dataset[1:,1]
location = dataset[1:,2]
datum = dataset[1:,3]
detail = dataset[1:,4]
statusrocket = dataset[1:,5]
costs_str = dataset[1:,6]
statusmission = dataset[1:,7]


sub = 'Success'
statusmission1 = np.char.find(statusmission, sub)
statusmission_bool = statusmission1 != -1
porcentagem = np.sum(statusmission_bool) / len(statusmission_bool) * 100
print(f'Porcentagem de missões com sucesso: {porcentagem:.2f}%')


costs = costs_str.astype(float)
cond = costs > 0
mediacosts = costs[cond].mean()
print(f'Media de gastos de uma missão: {mediacosts:.2f}')


sub1 = 'USA'
location1 = np.char.find(location, sub1)
usa = np.sum(location1 != -1)
print(f'Numero de missões realizadas pelos EUA: {usa}')


sub2 = 'SpaceX'
company1 = np.char.find(company, sub2)
spacex_bool = company1 != -1
costsspacex = costs[spacex_bool]
detailspacex = detail[spacex_bool]
idx_max = np.argmax(costsspacex)
print(f'Missão mais cara da SpaceX: {detailspacex[idx_max]}, Custo: {costsspacex[idx_max]}')


companies, qtd_missions = np.unique(company, return_counts=True)
for i in range(len(companies)):
    print(f'{companies[i]}: {qtd_missions[i]}')


sub3 = 'StatusRetired'
statusrocket1 = np.char.find(statusrocket, sub3)
statusrocket_bool = statusrocket1 != -1
porcentagemrocket = np.sum(statusrocket_bool) / len(statusrocket_bool) * 100
print(f'Porcentagem de missões com StatusRetired: {porcentagemrocket:.2f}%')


sub4 = 'Russia'
locationrussia = np.char.find(location, sub4)
locationrussia_bool = locationrussia != -1
qtd_russia = np.sum(locationrussia_bool)
print(f'Numero de missões realizadas pela Russia: {qtd_russia}')

maxcosts = costs.max()
maxcostsid = costs.argmax()
print(f'Missão mais cara do Dataset: {company[maxcostsid]}, ' 
      f'Custo: {maxcosts}')



