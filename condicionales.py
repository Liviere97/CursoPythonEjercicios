calificacion = int (input('cual es tu calificacion?'))
puntos_extras = False
#None null False
#Truthy o Falsy
#string vacio es Falsy , string con x cosa es verdadero
if calificacion >= 7 :
    print('pasaste')
elif calificacion >= 5 and calificacion < 7:
    print('si estudias pasas') 
#elif calificacion ==6 or puntos_extras:
    #print('puedes pasar')    
else:
    print('eres tonto') 