import os 

def validate_user_selection(selection):
   return True if  isinstance(selection, int) and selection > 0 and selection < 3 else False

def validate_user_wants_exit(selection):
     return selection == 3

def format_dict_to_string (dictionary):
   # attributes = []
    #for key, value in dictionary.items():
        #attributes.append(f'{key} {value}')
        #'|'.join(attributes)
    #return '|'.join(attributes)
    return '|'.join([f'{key} {value}' for key, value in dictionary.items()])

def format_string_to_dict(string):
    pairs = string.split('|')
    papita = {}
    for pair in pairs:
        [key,value]= pair.split(':')
        papita[key]= value 
    return papita    

def write_in_file(dictionary):
    file = open('papitas.txt','a')
    file.write(format_dict_to_string(dictionary)+'\n')
    print('\nPapita registrada con exito\n')
    file.close()

def read_file():
    papitas = []
    if os.path.exists('papitas.txt'): 
       file = open('papitas.txt','r') 
       papitas_lines = file.readlines()
       for line in papitas_lines:
           papitas.append(format_string_to_dict(line))
    return papitas            

def add_papita():
    #atributo:name , price , color 
    name = input('Cual es el nombre de la papita?:  ')
    price = float (input('cuanto cuesta: '))
    color = input ('cual es el color de la envoltura:  ')
    papita = {
        'name': name,
        'price': price,
        'color': color
    }    
    write_in_file(papita)   
def get_papitas():
    papitas = read_file()
    print("_______________________")
    print('Nombre\t\tPrecio\t\tColor\t\t')
    print()
    if len(papitas) > 0:
        for papita in papitas:
            print(f'{papita["name"]}\t\t{papita["price"]}\t\t{papita["color"]}')
        print("----------------------------")
    else:
        print('Aun no tiene papitas registradas')


def handle_user_selection(selection):
    if selection == 1:
        add_papita()
    else:
        get_papitas()
        pass 

def main():
    opt_exit = 'N'
    while opt_exit != 'S':
      papitas = read_file()
      print('papitas app')
      print('menu de opciones')
      print('1 agregar o registrar papitas')
      print('2 ver las papitas registradas')
      print('3 salir del programa')
      opt = int(input('QUE OPCION ELIGES? '))
      if validate_user_selection(opt):
          handle_user_selection(opt)
      elif validate_user_wants_exit(opt):
           opt_exit = 'S'
      else:
          print('OPCION INVALIDA') 
    print('Ejecución finalizada')   
main()