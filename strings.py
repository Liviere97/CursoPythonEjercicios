#CADENAS DE CARACTERES
#string = 'Hola mundo'
#string= input('Escribe un mensaje: ')
#primer_letra = string[0]
#longitud = len (string)
#ultimo_valor = string  [len(string) - 1]

#print (ultimo_valor)

#Slices
mensaje = 'Aprendiendo a programar en python'
slc_1 = mensaje[12:]
slc_2 = mensaje[:21]
slc_3 = mensaje [6:17]
#print (slc_1)
#print (slc_2)
#print (slc_3)

#SPLIT

splited = mensaje.split (" ")
print (splited)

#LISTAS
lista = ['palabra' , 3 , 5.43 , True ,['soy','livi','manzano']]
#print (lista[4][1])
#lista_anidada = lista[4]
#lista_anidada[1]
print (lista)

#METODOS DE LAS LISTAS
#pop quita el ultimo elemento
lista.pop()
nueva_lista = lista.pop()
print (nueva_lista)
print(lista)

#append agregar un elemnto al final
lista.append(False)
print(lista)
# join toma una lista de strings y lo convierte a un string
lista_string = ['1','2','3','4']
separador = '-'

lista_joineada = separador.join(lista_string)
print (lista_joineada)