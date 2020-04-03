#4/3 pi * r**3
import math

print ('Vamos a calcular el volumen de una esfera') 
radio = float(input('Ingresa el valor del radio de la esfera en cm '))
print('El valor de pi es de ' , math.pi)
volumen  = (4/3 * math.pi) * (radio ** 3)
print ('El volumen de la esfera es ' ,'{:0.2f}'.format(volumen),'cm' )
