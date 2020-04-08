
nombre= input('INGRESA TU NOMBRE:  ')
apellidos =input ('INGRESA TUS APELLIDOS: ')
edad=input('INGRESA TU EDAD: ')
email=input('INGRESA TU EMAIL: ')

first_name = nombre
last_name = apellidos
age= edad
EMAIL= email  

usuario = {}

usuario [first_name ]
usuario [last_name ]
usuario [age]
usuario [EMAIL]
        
#print(usuario)
for key, value in usuario.items():
    print(f'{key.upper()}: {value}')
#for key, value in usuario.items():
    #print("#####################")
    #print("key:", key)
    #print("value", value)
