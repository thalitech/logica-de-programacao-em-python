import random

winner = ''

random = random.randint(0,2)

if random == 0:
    computador = 'pedra'
elif random == 1:
    computador = 'papel'
else:
    computador = 'tesoura'
print('Escolha do computador: ',computador)

usuario = ''
    
while (usuario != 'pedra' and
       usuario != 'papel' and
       usuario != 'tesoura'):
    usuario = input('Escolha um tipo: Pedra, papel, tesoura: ')

if computador == usuario:
        winner = 'Tie'
elif computador == 'papel' and usuario == 'pedra':
        winner = 'computer'
elif computador == 'pedra' and usuario == 'tesoura':
        winner = 'computer'
elif computador == 'tesoura' and usuario == 'papel':
        winner = 'computer'
else:
        winner = 'User'

if winner == 'Tie':
        print('escolhemos igual', computador + ',play again')
else:
        print(winner, 'o computador escolhe')

#papel 1 > pedra 0
#pedra 0 > tesoura 2
#tesoura 2> papel 1
