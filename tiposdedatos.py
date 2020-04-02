#print('Hola mundo')
#tipos de datos

entero=15
flotantes= 5.32151
string ='texto'
booleano= True

#operadores
suma = 4 +5
resta = 5-4
multiplicacion = 5*4
potencia = 5 ** 2
division = 10/2
division_exacta = 5//2
modulo = 10 % 2 

#print('El valor de la suma es : ' , suma)
#print ('Ingresa cifras a sumar')
print ('Ingresa lo que se te pide')
numero_1 = float (input('Ingresa un numero: '))
numero_2  = float (input('Ingresa otro numero: '))

sumita = numero_1 + numero_2
mul = numero_1 * numero_2
res = numero_1 - numero_2
po = numero_1 ** numero_2
div = numero_1 / numero_2
exac =  numero_1 // numero_2
mod = numero_1 % numero_2

print('RESULTADOS')

print('La suma es de', '{:0.3f}'.format(sumita))
print('La multiplicacion  es de', '{:0.3f}'.format(mul))
print('La resta es de', '{:0.3f}'.format(res))
print('La potencia es de', '{:0.3f}'.format(po))
print('La division es de', '{:0.3f}'.format(div))
print('La division exacta es de', '{:0.3f}'.format(exac))
print('El modulo  es de', '{:0.3f}'.format(div))




