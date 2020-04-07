#FOR
for i in range(5): #Empieza en 0 y termina en 5
 #for (var i= 0; i<5 )
  print('Hola ususario', i)

print('////////////')
print('TABLA DEL 4')
for i in range(1,10): #empieza en 1 y termina en 10
  print(f'4 x {i} = {4*i}')
print('//////////')
print('numeros pares hasta el 50')

for i in range(1,51,2):
    print(i)

print('=======================')
print('lista de egresados')
personas= ["Livi","Felipe","Fer"]
for persona in personas:
    print('ING',persona)

print('=======================')

estudiantes = [
    ['Livi',[10,10,10]],
    ['Felipe',[7,10,9]],
    ['Fer',[10,9,10]],
    ['Sahara',[10,10,10]],
    ['Maria',[8,10,10]],
]

for estudiante in estudiantes:
    print('*******************************')
    print('Nombre del alumno:', estudiante[0])
    print('calificaciones')
    notes = estudiante [1]
    #print(notes)
    for i, note in enumerate(notes):
        print(f'Calificacion #{i + 1}: {note}')
average = sum(notes)/len(notes)
#print ('Promedio',average)
#if average > 6:
    #print('APROBADO')
#else:
    #print('REPROBADO')    
#operador ternario
print(f'PROMEDIO: {average: .2f} - {"APROBADO" if average > 6 else "REPROBADO"}')

print("===============================")
print("USANDO EL WHILE")

# Script to greet people. The program will stop when the user says S, if the option entered for the user is invalid, we have a nested while.
opt = 0
while opt != 'S':
  name = input("Por tu nombre pa saludarte, compa: ")
  print("Hola!", name)
  exit = input("Quieres salirte alv? (S/N): ")
  while exit != "S" and exit != "N":
    print("No mames, ingresa una opción válida")
    exit = input("Quieres salirte alv? (S/N): ")
  opt = exit
print("Gracias por dejame saludaaarte")

print('Vamos a la iglesia')
print('Me das tu diezmo?')

acum = 0
payments = 0

while payments < 10:
  pay = float(input('Ingresa tu diezmo a la iglesia: '))
  acum += pay
  payments += 1
print(f'Total de lo que le has pagado a la Iglesia: {acum:.2f}')

print("===============================")
print("EL MISMO PERO CON FOR")

print('Vamos a la iglesia uhuuhoho')
print('Me das tu diezmo o te lleva satanas :)')
i = 0
for i in range(0,11):
    diezmo= float(input('Dame tu dinero:'))
    i+=diezmo
print(f'Tu linda donacion es de : {i:.2f}')
print('gracias mil estimado pecadors')