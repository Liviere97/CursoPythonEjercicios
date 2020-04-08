usuario = {
    'first_name': 'Livi',
    'last_name': 'Mercado Manzano',
    'age': 22,
    'birth_date': '1997-12-01',
     
}
print(usuario)

#get a key a dict como acceder a un atributo dentro de un diccionario

#print(usuario['first_name'])
#que pasaria si tratao intentar una llave que no existe
#print(usuario['gender'])#trazar un errror
#como checar si un atribiuto existe en un diccionario?
#print('gnder' in usuario)
#print('first_name 'in usuario)

if 'gender' in usuario: 
 print (usuario['gender'])
else:
    print('gender no existe')

if 'last_name ' in usuario:
    print(usuario['last_name'])
else:
    print('last name no existe')

   #

print(usuario.get('country', 'mexico'))

#como agregar llaves al diccionario/nuevo elemento

usuario['email']='livi@hotmail.com'
#print(usuario)

#como actualizar atributos existentes
usuario['email']='livi@gmail'
#print(usuario)

#como eliminiar atributos
del usuario['email']
#print(usuario)

profile = {
    'profile_foto': 'perfil.jpg',
    'RFC': 'MEML007623677',
    'hobbies': 'leer y hacer ejecrcicio',
}
#concatenar 
usuario.update(profile)
print(usuario)

#como hacer loop con llaves en un diccionario
for key, value in usuario.items():
    print("#####################")
    print("key:", key)
    print("value", value)
