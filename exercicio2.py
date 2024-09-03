import numpy as np 

matriz = [[37,  42,  28,  95,  14,  18,  89,  83,  22,  20],
          [63,  91,  75,  9,   58,  25,  72,  59,  52,  92]]

print ('Qual ponto x,y tem o maior valor de x?')

linha = 0;
col = 0;
for i in range(len(matriz)):
   for j in range(len(matriz[i])):
      if(matriz[i][j]> matriz[linha][col]):
         linha = i
         col = j

print(f"Maior elemento: {matriz[linha][col]}")
print ('') 

print ('Qual ponto x,y tem o menor valor par de y? R:')
linha = 0;
col = 0;
par = []
for i in range(len(matriz)):
   for j in range(len(matriz[i])):
      if(matriz[i][j]< matriz[linha][col]):
         linha = i
         col = j
      if (matriz[i][j] % 2 == 0):
                par.append(matriz[i][j])
print(f"Menor elemento par: {(min(par))}")
print ('')


print ('Qual ponto x,y que tem a maior soma (x+y)? R:')


A = np.array([[37,  42,  28,  95,  14,  18,  89,  83,  22,  20]]); 
 
B = np.array([[63,  91,  75,  9,   58,  25,  72,  59,  52,  92]]);

soma = A+B
print(f"Elemento com Maior Soma: {(max(soma))}")

