#1- Faça um Programa que mostre a mensagem "Alo mundo" na tela.

#print("Alo mundo!")

#2- Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].

#numero = input('Insira um numero: ')
#print(f"O numero informado foi {numero}")

#3- Faça um Programa que peça dois números e imprima a soma.
# numero1 = input('Insira o primeiro numero: ')
# numero2 = input('Insira o segundo numero: ')
# num1_int = int(numero1) # converte string/texto para inteiro
# num2_int = int(numero2)
# soma = num1_int + num2_int
# print(f"A soma dos dois numeros é ", soma)

#4- Faça um Programa que peça as 4 notas bimestrais e mostre a média.
# numero1 = input('Insira o primeira nota: ')
# numero2 = input('Insira o segunda nota: ')
# numero3 = input('Insira o terceira nota: ')
# numero4 = input('Insira o quarta nota: ')
# num1_int = int(numero1) # converte string/texto para inteiro
# num2_int = int(numero2)
# num3_int = int(numero3)
# num4_int = int(numero4)
# soma = num1_int + num2_int + num3_int + num4_int
# media = soma / 4
# print(f"A media é ", media)

#5- Faça um Programa que converta metros para centímetros.
# comprimento = input('Insira o comprimento em metros: ')
# comp = int(comprimento) # converte string/texto para inteiro
# conversao = comp * 100
# print(f"o comprimento em centimetros é ", conversao)

#6- Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
# diametro = input('Insira o diametro do circulo: ')
# dia = int(diametro ) # converte string/texto para inteiro
# raio = dia ** 2
# pi = raio * 3.14
# print(f"Area do circulo é ", pi)

#7- Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
# quadrado = input('Insira o area de um quadrado: ')
# quadrado = int(quadrado) # converte string/texto para inteiro
# area = quadrado ** 2
# dobro = area * 2
# print(f"Area do quadrado é", dobro)

# 8 - Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
# valor = input('quanto você ganha por hora: ')
# horas = input('Insira o seu numero de horas trabalhadas no mes: ')
# converte_valor = int(valor) # converte string/texto para inteiro
# converte_horas = int(horas) # converte string/texto para inteiro
# salario = converte_valor * converte_horas
# print(f"Seu salario mensal é", salario)

# 9 - Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a temperatura em graus Celsius. C = (5 * (F-32) / 9).
# temp = input('Informe a temperatura em graus Farenheit: ')
# t = float(temp) # converte string/texto para inteiro
# c = 5 * (t-32) / 9
# print(f"a temperatura em graus Celsius é ", c)

# 10 - Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Farenheit.
# temp = input('Informe a temperatura em graus Celsius: ')
# t = float(temp) # converte string/texto para inteiro
# f = (t * 9/5) + 32
# print(f"a temperatura em graus Farenheit é ", f)

# 11 - Faça um Programa que peça 2 números inteiros e um número real. 
# Calcule e mostre: o produto do dobro do primeiro com metade do segundo.
#  a soma do triplo do primeiro com o terceiro. o terceiro elevado ao cubo.
# # numero1 = input('Insira o primeiro numero inteiro: ')
# # numero2 = input('Insira o segundo numero inteiro: ')
# # numero3 = input('Insira o terceiro numero real: ')
# # num1_int = int(numero1) # converte string/texto para inteiro
# # num2_int = int(numero2)
# # num3_int = int(numero3)
    
# # a = (2*num1_int)*(num2_int/2)
# # b = (3*num1_int)+num3_int 
# # c = num3_int*num3_int*num3_int
    
# # print("\n\nO produto do dobro do primeiro com metade do segundo é igual a ",a)
# # print("\nA soma do triplo do primeiro com o terceiro é igual a ",b)
# # print("\nO terceiro elevado ao cubo é igual a ",c)

# 12- Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58
# numero1 = input('Insira a sua altura: ')
# altura = float(numero1) # converte string/texto para inteiro
# resultado = (72.7*altura) - 58
# print("\n\no peso ideal é ",resultado)

# 13- Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas: Para homens: (72.7h) - 58 Para mulheres: (62.1h) - 44.7

# sexo = input('voce é homem ou mulher? digite h ou m')
# if sexo == 'h':
#     numero1 = input('Insira a sua altura: ')
#     alth = float(numero1) # converte string/texto para inteiro
#     homens =  (72.7*alth) - 58
#     print("\n\nO peso ideal para homens é ", homens)
# elif sexo == 'm':
#     numero2 = input('Insira a sua altura: ')
#     altm = float(numero2) # converte string/texto para inteiro
#     mulheres = (62.1*altm) - 44.7
#     print("\n\nO peso ideal para mulheres é ",mulheres)

# 14- João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar
#  o rendimento diário de seu trabalho.
# Toda vez que ele traz um peso de peixes maior que o estabelecido pelo 
# regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma
#  multa de R$ 4,00 por quilo excedente.
#João precisa que você faça um programa que leia a variável peso
#  (peso de peixes) e calcule o excesso.
#Gravar na variável excesso a quantidade de quilos além do limite
#  e na variável multa o valor da multa que João deverá pagar. 
# Imprima os dados do programa com as mensagens adequadas.
# limitekilo = float(50)
# multa = float(4)

# pescado = input('Informe quantos kilos voce pescou: ')
# conv = float(pescado)
# if conv > limitekilo:
#     excedente = conv - 50
#     fatura = excedente * multa
#     print ('A sua multa é no valor de ', fatura)
# elif conv <= 50:
#     print('Pescado está dentro do limite!')

#15- Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
#Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda,
#  8% para o INSS e 5% para o sindicato, faça um programa que nos dê: salário bruto. quanto pagou ao INSS.
#  quanto pagou ao sindicato. o salário líquido. calcule os descontos e o salário líquido, conforme a tabela abaixo:
#+ Salário Bruto : R$
#- IR (11%) : R$
#- INSS (8%) : R$
#- Sindicato ( 5%) : R$
#= Salário Liquido : R$
#Obs.: Salário Bruto - Descontos = Salário Líquido.

# ir = float(11/100)
# inss = float(8/100)
# sind = float(5/100)

# valor = input('quanto você ganha por hora: ')
# horas = input('Insira o seu numero de horas trabalhadas no mes: ')
# converte_valor = int(valor) # converte string/texto para inteiro
# converte_horas = int(horas) # converte string/texto para inteiro
# salariobruto = converte_valor * converte_horas
# print(f"Seu salario bruto mensal é", salariobruto)
# descontoir = salariobruto * ir 
# print(f"Seu desconto do IR (11%) é", descontoir)
# descontoinss = salariobruto * inss
# print(f"Seu desconto do INSS (8%) é", descontoinss)
# descontosind = salariobruto * sind 
# print(f"Seu desconto do sindicato (5%) é", descontosind)
# salarioliquido = salariobruto - descontoir - descontoinss - descontosind
# print(f"Seu salario liquido é", salarioliquido)

#16- Faça um programa para uma loja de tintas. 
# O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para
#  cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros,
# que custam R$ 80,00.
# Informe ao usuário a quantidades de latas de tinta
#  a serem compradas e o preço total.
# litro = float
# cobertura = 3 
# lata = 18
# custo = 80
# metros = input('Insira o tamanho em metros quadrados da area a ser pintada: ')
# converte_valor = float(metros) # converte string/texto para decimal
# litros =  converte_valor / 3
# quantlatas = litros / 18
# precototal = quantlatas * 80
# print(f"A quantidade de latas a serem compradas é", quantlatas)
# print(f"O valor total é", precototal)

#17 -Faça um Programa para uma loja de tintas.
# O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros,
# que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# comprar apenas latas de 18 litros;
# comprar apenas galões de 3,6 litros;+
# misturar latas e galões, de forma que o preço seja o menor.
#     Acrescente 10% de folga e sempre arredonde os valores para cima,
#     isto é, considere latas cheias.

# #18- Ano nascimento
# anonasc = input('Insira o ano do nascimento: ')
# nasc = int(anonasc) 
# anocalc = input('Insira o ano para calculo da idade: ')
# calc = int(anocalc) 
# if calc >= nasc:
#     resultado = calc - nasc
#     print('voce teria a idade de ', resultado)
# elif calc < nasc:
#     print('Data informada é menor que a data de nascimento fornecida')




