from  random import randint


jugador = int(input('que opcion eliges (1)Piedra (2)papel (3)tijeras'))
compu = randint (1,3)

if jugador == 1 and compu ==1:
 print('empate')
if  jugador == 2 and compu == 2:
  print('')