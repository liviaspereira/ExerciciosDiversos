'''Guarde na variável precos_dobro uma nova lista que seja a lista 
lista_precos com seus elementos multiplicados por 2.'''

lista_precos = [30.5, 20.2, 19.99, 9.99, 192.10, 81,10, 42.42]

lista_dobro = []
for valores in lista_precos:
    dobro = valores * 2
    lista_dobro.append(dobro)
print(lista_dobro)


lista_dobro = [valores * 2 for valores in lista_precos]


