# FUNCIONES QUE HACEN LAS OPERACIONES

# Realizar la suma de todos los numeros
def sum_num(numeros):
    suma = 0
    for n in numeros:
        suma = suma + int(n)
    return suma

# Calcular el promedio de todos los numeros
def prom_num(suma, longitudnum):
    promedio = suma/longitudnum
    return promedio

# Calcular la multiplicacion de todos los numeros
def mult_num(numeros):
    mult = 1
    for n in numeros:
        mult = mult * int(n)
    return mult

# Elevar cada uno de los números al cuadrado
def cuadrado_n(n):
    cuad = int(n) ** 2
    return cuad
    
# Calcular el factorial de cada uno de los números
def fact_num(n):
    tope=int(n)
    fact = int(n)
    for i in range(1,tope):
        fact = fact * i
    return fact

    
# FUNCIONES QUE IMPRIMEN LOS RESULTADOS
def imp_sum(suma):
    print("El resultado de la suma es:", suma)

def imp_prom(promedio):
    print("El resultado del promedio es:", promedio)

def imp_mul(mult):
    print("El resultado de la multiplicacion es:", mult)

def imp_cuad(cuad,n):
    print(f'El resultado del cuadrado del numero {n} es: {cuad}')

def imp_fac(fact,n):
    print(f'La factorial del numero {n} es: {fact}')

# FUNCION PRINCIPAL
 
def main():
    print("Ejm: 2,3,5,4,3,6")
    num = input("Escribe los numeros a jugar con ellos, separados por una coma: ")
    #QUITAR LAS COMAS
    numeros = num.split(",")
    #NUM DE DIGITOS
    longitudnum = len(numeros)
    #Llamando las funciones
    suma = sum_num(numeros)
    promedio = prom_num(suma,longitudnum)
    mult = mult_num(numeros)
    imp_sum(suma)
    imp_prom(promedio)
    imp_mul(mult)
    for n in numeros:
        cuad = cuadrado_n(n)
        imp_cuad(cuad,n)
    for n in numeros:
        fact = fact_num(n)
        imp_fac(fact,n)



    
    

main()
