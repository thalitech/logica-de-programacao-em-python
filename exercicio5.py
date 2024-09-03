#digite multiplo de 9, parabens esse numero é multiplo de 9 se nao errou

numero = input('Escolha numero multiplo de 9: ')
num = int(numero)
while (num % 9 == 0):
    if num % 9 == 0:
        print ('Parabens é multiplo de 9: ', numero)
    else:
        print ('Escolha numero multiplo de 9 novamente: ', numero)
    numero = input('Escolha numero multiplo de 9: ')
    num = int(numero)
