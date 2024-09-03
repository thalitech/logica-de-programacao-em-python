scores = [60,50,60,58,54,54,
          58,50,52,54,48,69,
          34,55,51,52,44,51,
          69,64,66,55,52,61,
          46,31,57,52,44,18,
          41,53,55,61,51,44]

custos = [.25,.27,.25,.25,.25,.25,
         .33,.31,.25,.29,.27,.22,
         .31,.25,.25,.33,.21,.25,
         .25,.25,.28,.25,.24,.22,
         .20,.25,.30,.25,.24,.25,
         .25,.25,.27,.25,.26,.29]

total= len(scores)
print ('total scores',total)

length = len(scores)


#le todas as posicoes do array while
i = 0
while (i < length):
    print('solution #' + str(i),'score',scores[i])
    i = i+1
    
#le todas as posicoes do array for
length = len(scores)
for i in range(length):
    print('solution 2 #' + str(i), 'score:', scores[i])
 
high_scores = 0

length = len(scores)
for i in range(length):
    print('buble solution #' +str(i),'score:', scores[i])
    if scores[i] > high_scores:
        high_scores = scores[i]
        
best_solutions = []
for i in range(length):
    if high_scores == scores[i]:
        best_solutions.append(i)
        
print('highest bubble score', high_scores)
print('Bubbles test', length)
print ('indice dos bubbles mais alto',best_solutions)
#total:36
#scoremais alto 69
#solucoes com escore alto [11,18]

custo = 100.0
muitoefetivo = 0

for i in range(length):
    if scores[i] == high_scores and custos[i] < custo:
        muitoefetivo = i
        custo = custos[i]
print('Solution', muitoefetivo, 'é muitoefetivo com o custo de ', custos[muitoefetivo])


#Reescrevendo o código com uma melhor solução de custo beneficio entre as listas

custo = 100.0
maisefetivo = 0

for i in range(len(best_solutions)):
    index = best_solutions[i]
    if custo > custos[index]:
        maisefetivo = index
        custo = custos[index]

print('Solution', maisefetivo, 'é mais efetivo com o custo de ', custos[maisefetivo])





