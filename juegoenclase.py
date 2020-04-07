# Crear el juego de piedra papel o tijera
# Pedirle al jugador que eliga su opcion
# Hacer que la computadora eliga una accion
# Crear los casos diferentes para cada una de las opciones que elija el usuario y la computadora
# Si el usuario elije piedra y la computadora también, es empate
# Si la computadora eligio papel, gana la computadora
# Si la computadora eligio tijeras, gana el usuario

from random import randint

name = input('Hola, cual es tu nombre? ')
print('Hola', name)

jugador = int(input('Que arma escoges? (1)Piedra (2)Papel (3)Tijeras '))

if(jugador == 1 or jugador == 2 or jugador == 3):
  computadora = randint(1, 3)

  if computadora == 1:
    com = "Piedra"
  elif computadora == 2:
      com = "Papel"
  elif computadora == 3:
      com = "Tijeras"

  print('La computadora eligio', com)
  if jugador == 1:
    if computadora == 1:
      print('Es un empate')
    elif computadora == 2:
      print('La computadora gana')
    else:
      print(name, 'gana!')
  elif jugador == 2:
    if computadora == 2:
      print('Es un empate')
    elif computadora == 3:
      print('La computadora gana')
    else:
      print(name, 'gana!')
  elif jugador == 3:
    if computadora == 3:
      print('Es un empate')
    elif computadora == 1:
      print('La computadora gana')
    else:
      print(name, 'gana!')
else:
  print('Ingrese un valor correcto')

# numero_aleatorio = randint(1,10)
# print(numero_aleatorio)