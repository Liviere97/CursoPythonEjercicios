class pizza:
    #tamaño
    #ingredientes
    #precio
    
    
    #Constructor
    ingrediente=['peperoni','hawaiana' , 'quesos']
    tamaños =['chica','Grande' , 'familiar']

    def __init__ (self, tamaño , ingredientes , precio):
        self.tamaño = self.tamaños[tamaño-1]
        self.ingredientes = self.ingrediente[ingredientes-1]
        self.precio = precio 
        
    
        # Getters

    def get_entrada(self):
        print ('TAMAÑO :', self.tamaño)
        print('INGREDIENTES', self.ingredientes)
        print('PRECIO',self.precio) 

def main():
    print('1.- chica')
    print('2.- Grande')
    print('3.-familiar')
    tamaño = int (input('ingresa el tamaño de su pizza: ')) 
    precio = int (input('ingrese precio: '))
    print('1.- peperoni')
    print('2.- hawaiana')
    print('3.-quesos')
    ingredientes = int(input('ingrese los ingredientes :'))  
    print ('SU ORDEN CONSTA DE : ') 

    pizzeria = pizza(tamaño , ingredientes , precio)
    pizzeria.get_entrada()

main ()
