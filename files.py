#ESCRIBIR IIR EN UN ARCHIVO DE TEXTO
#r- abrir un archivo de lectura
#w - abrir un archivo para escritura , si no existe , crea un nuevo archivo,
#    si existe 
def texto():
    archivo = open("texto.txt","rb")
     
    contenido = archivo.read()
    print(contenido)
    archivo.close()

def create():
    #archivo = open("archivo.txt ", "x")
    archivo = open("archivo_nuevo.txt ", "x+")
    archivo.write("escribe esto")
    contenido= archivo.read()
    print(contenido)
    archivo.close()

def read():
    archivo = open("texto.txt ", "r")
    if archivo.mode == 'r':
        content = archivo.read()
        print(content)
    archivo.close()    
def append():
    archivo = open("texto.txt", "a+")

    for i in range(5):
        archivo.write(f"linea apendada {i+1}\n")
    archivo.close() 

def main():
    archivo = open ("texto.txt", "w+")

    for i in range(10):
        archivo.write(f"TEXTO ALEATORIO {i+1}\n")
    archivo.close()    
texto() 