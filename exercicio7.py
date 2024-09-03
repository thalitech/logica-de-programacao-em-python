#Faça um Programa que peça dois números e imprima o maior deles.

num1=0
num2=1


while (num1 != num2):
    numero1 = input('informe o primeiro numero: ')
    num1 = int(numero1)
    numero2 = input('informe o segundo numero: ')
    num2 = int(numero2)
    
    if num1 > num2:
        print ('Primeiro numero',num1,' maior que segundo',num2)

    elif num2 > num1:
        print ('segundo numero',num2,' maior que primeiro',num1)
    else:
        print ('Numeros iguais. tchau ')

    
