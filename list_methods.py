#metodos de listas
lista = ['livi', 'shara', 'feliipe']
print(lista)

#nos regresa el inice del elemento que queremos buscar en una lista existente
shara_index = lista.index('shara')
print(shara_index)

#agregar un elementoal final de la lista
lista.append('pablito')
print(lista)
#EXTIENDE UNA LISTA , GAREGANDO AL FNAL TODOS LOS NUESVOS ELEMENTOS
lista_extra = ['CALEB','SIMBA','MARIGELI']
lista.extend(lista_extra)
print(lista)
#INSTERTA UN ELEMENTO EN LA LISTA EN EL INDICE INDICADO
lista.insert(shara_index, 'shara')
print(lista)
#REGRESA EL NUMERODE VECES QUE ENCUENTRA UN ELEMENTO EN LA LISTA
shara_count = lista.count('shara')
print(shara_count)
#ELIMINAR EL PRIMER ELEMENTO DE LALISTA QUE CONCUERDE CON EL PARAMETRO RECIBIDO
lista.remove('pablito')
print(lista)
#ELIMINAR UN ELEMENTO DE LA LISTA EN EL INDICE  INDICA Y REGRESA EL ELEMENTO ELIMINADO
elemento_livi = lista.pop()
print(lista)
print(elemento_livi)

lista.pop()
print(lista)

lista.pop(shara_index)
print(lista)

#INVERTIR EL ORDEN DE LOS ELEMENTOS EN UNA LISTA
lista.reverse()
print(lista)
#ORDENA LOS ELEMENTOS DE UNA LISTA EN ORDEN ESECIFICO DESCENDENTE O ASENDENTE
lista.sort()
#lista.sort(reverse=True)
print(lista)
#REGRESA UNA COPIA DE UNA LISTA
copy = lista.copy()
#copy =lista
print (copy)
#COMPROBAMOS QUE NO SE MODIFICO LA COPIA gracias a el metodo copy()
lista.append('fulana')
print(lista)
print(copy)

#ELIMINA TODOS LOSELEMENTOS DE UNA LISTA
