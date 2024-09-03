
x = [37,  42,  28,  95,  14,  18,  89,  83,  22,  20]
y = [63,  91,  75,  9,   58,  25,  72,  59,  52,  92]

print ('Qual ponto x,y tem o maior valor de x? R:')
print (max(x))
print (max(y))

print ('Qual ponto x,y tem o menor valor par de y? R:')

pary = []
for valor in y:
    if valor % 2 == 0:
          pary.append(valor)
print(min(pary))

parx = []
for valor in x:
    if valor % 2 == 0:
          parx.append(valor)
print(min(parx))

print ('Qual ponto x,y que tem a maior soma (x+y)? R:')
print(max(y))
print(max(x))
