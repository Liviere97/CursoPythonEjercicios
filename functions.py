#ARGUMENTOS
#PARAMETROS: lo que va arecibir la variable
#ARGUMETO:
def print_name(name, last_name):
    print("hola", name, last_name)
#print_name("livi")
#print_name("mari")
#print_name("mari" , "geli") 

#argumentos arbitrarios

#ponemos asterisco antes del nombre del parametro cuando no se conoce el numero de argumentos
#esto hara que reciba una tupla de argumentos
def name(*kids):
    print("el niño mas  peque es" , kids[0])
#name("arturo","melo", "topi")    

def morritos(morrito1 , morrito2 , morrito3):
    print("el mas cool es " , morrito2)
#morritos(morrito2 = "melo ," morrito1="yo", morrito3="tu")

def pais(pais= "coatepec"):
    print("yo vivo en : " , pais)

#pais() 
#pais("mi casa")  

#no es necesario definir el tipo de datos que va a recibir la funcion 
def comida(comida):
    for comidita in comida:
      #print(comidita)
#comida(["pizza","tacos","enchiladas"])    

#RGRESAR ALGUN VALOR LLAMANDO A UNA FUNCION
def multiplicacion(x):
    return 5 * x
print(multiplicacion(3))

def pruebita():
    pass 

#pruebita()

#RECURSIVIDAD

def factorial(x):
    if x==1:
        return 1
    else:
        return x * factorial (x-1)
#print(factorial(5))            

#lista =["livi ", "felipe","caleb"]
#for elemento in lista:
    #print(elemento)
#TAREA HACER ESTE FOR EN RECURSIVIADA
#lista =["livi ", "felipe","caleb"]
#def elemento(lista):
    #print(elemento)