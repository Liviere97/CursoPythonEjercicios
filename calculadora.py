def suma(num1 , num2):
    return num1 + num2

def resta(num1 , num2):
    return num1 - num2

def multiplicacion(num1 , num2):
    return num1 * num2

def divison(num1 , num2):
    return num1 / num2   

def division_exacta(num1 , num2):
    return num1 // num2

def elevar_cuadrado(num1):
    return num1 ** 2

def print_values(name, value):
    print (f'el resultado de la {name} es : {value}')

def main():

    num1 = int(input('DAME UN NUMERO'))
    num2 = int(input('DAME OTRO NUMERO'))

    sumita = suma(num1, num2)
    restaa = resta(num1, num2)
    multi =multiplicacion(num1, num2)
    divi = divison(num1, num2)
    divi_exac = division_exacta(num1, num2)
    num1_cuadrado= elevar_cuadrado(num1)
    num2_cuadrado= elevar_cuadrado(num2)

    print_values('suma', sumita)
    print_values('resta', restaa)
    print_values('multiplicacion', multi)
    print_values('division', divi)
    print_values('division exacta', divi_exac)
    print_values('elevacion de un numero al cuadrado',num1_cuadrado)
    print_values('elevacion de un numero al cuadrado', num2_cuadrado)
    

main()