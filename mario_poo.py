import random

class MarioBross:

    #Constructor
    personajes=['normal','grande' , 'fuego']
    def _init_(self ,vidas , monedas , personaje ):
        self.vidas = vidas
        self.monedas = monedas
        self.personaje = personajes[personaje-1]

    def get_actual_status(self):
        print ('No.vidas ', self.vidas)
        print('No.monedas:', self.monedas)
        print('personaje actual:',self.personaje)

    def killed(self):
        self.vidas =- 1
        self.personaje = self.personajes [0]
        print ('me mori')
        if self.vidas ==0:
            print('gracias por jugar , F')   

    def eat_green_mushroom(self):
        self.vidas += 1
        print('tengo una oportunidad mas pa morir')

    def get_coin(self):
        self.monedas +=1
        print("+1 moneda")
        if self.monedas ==100 :
            self.eat_green_mushroom()
            monedas = 0
    def eat_red_mushroom(self):
        print("estupefacientes color rojo")
        if self.personaje == self.personajes[0]:
            self.personaje = self.personajes[1]


    def eat_flower(self):
        print("Florecita para el estomago")
        if self.personaje == self.personajes[0]:
            self.personaje = self.personajes[1]
        elif self.personaje == self.personajes[1]:
            self.personaje = self.personajes[2]

    def attacked_by_something(self):
        print("me pegaron")
        if self.personaje == self.personajes[2]:
            self.personaje = self.personajes[1]
        elif self.personaje == self.personajes[1]:
            self.personaje = self.personajes[0]
        elif self.personaje == self.personajes[0]:
            self.killed()            

    def fall(self):
        print('Amá, me caí')
        self.killed()



def main():
    vidas = int (input('ingresa el numero de vidas actual')) 
    monedas= int (input('ingresa el numero de monedas'))
    print('1.- Normal')
    print('2.- Grande')
    print('3.-Fuego')
    personaje = int(input('ingresa el personaje de mario actual :'))

    mario_bros = MarioBross(vidas , monedas ,personaje)       


    while (opc!= 'N'):
        random_option = random.randint(1, 7)
        if random_option == 1:
            mario_bros.eat_red_mushroom()
        elif random_option == 2:
            mario_bros.eat_green_mushroom()
        elif random_option == 3:
            mario_bros.get_coin()
        elif random_option == 4:
            mario_bros.eat_flower()
        elif random_option == 5:
            mario_bros.attacked_by_something()
        elif random_option == 6:
            mario_bros.fall()
        else:
            mario_bros.killed()

        mario_bros.get_actual_status()
        print("------------------------")
        opc = input('¿Deseas seguir jugando con Mario? (S/N): ')

    print('De nada vuelva pronto')

main()