
smoothies = ['coconut', 'strawberry', 'banana','tropical','acai berry']

has_coconut = [True,False,False,True,False]

i=0

while i < len(has_coconut):
    if has_coconut[i]:
            print(smoothies[i], 'contains coconut')
    i = i+1

length = len(has_coconut)
for i in range(length):
        if has_coconut[i]:
            print(smoothies[i], 'contains coconut')
            
for smoothie in smoothies:
    output = 'we serve ' + smoothie
    print(output)

# imprime dentro de um range
for i in range(5):
    print('Interating through',i)

# imprime dentro de um range inicial e final
for i in range(5,10):
    print('Interating through',i)

# imprime dentro de um range inicial e final com intervalos
for i in range(5,10,2):
    print('Interating through',i)

# imprime de tras pra frente
for i in range(10,0,-1):
    print('Interating through',i)

# imprime começando com numeros negativos
for i in range(-10,2):
    print('Interating through',i)

#imprime indice de cada um
length = len(smoothies)
for i in range(length):
    print('Smoothie #',i,smoothies[i])
