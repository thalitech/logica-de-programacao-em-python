#Adicionar itens na lista

menu = []

menu.append('Burguer')
menu.append('Sushi')
print(menu)

#repetir itens da lista
mystery = ['secret' * 5]
print(mystery)

#repetir itens da lista
mystery = 'secret' * 5
print(mystery)

#deletar item da lista
del menu[0]
print(menu)

#adicione uma lista a outra
menu.extend(['BBQ', 'Tacos'])
print(menu)

#juntar listas com operador+
menu = menu + ['BBQ', 'Tacos']
print (menu)

#Insira itens em sua lista
menu.insert(1, 'Stir Fry')
print(menu)
