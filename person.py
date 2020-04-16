class Person:

    #Constructor
    def _init_(self , first_name , last_name , curp ,email,age,height,nacionality):
        self.first_name = first_name
        self.last_name = last_name
        self.curp = curp
        self.email = email
        self.age = age
        self.height = height
        self.nacionality = nacionality

    #GETTERS(METODO POR CADA ATRIBUTO)
    def get_first_name (self):
        return self.first_name
    #SETTERS (ACTUALIZAR LOS VALORES)
    def set_first_name(self , first_name):
        self.first_name = first_name

    def present_me(self):
        print(f'Hola mi nombre es : {self.first_name} {self.last_name}')
        print(f'mi CURP : {self.curp}')
        print(f'actualmente tengo {self.age} años y soy de {self.nacionality}')
        print(f'mido {self.height} metros y mi correo es  {self.email}')
        print('es un gusto')

class Student(Person):
    def _init_(self, id,career,semester,group , *args):
        super (Student, self)._init_(*args)
        self.id = id
        self.career = career
        self.semester = semester
        self.group = group
    def student_info(self):
        print(f'mi matricula es  : {self.id}')
        print(f'mi carrera es : {self.career}')
        print(f'mi semestre : {self.semester}')
        print (f'mi grupo : {self.group}')         

def main ():
    #person = Person ('livi ' , 'mercado','memlhfg90778', 'livi@hotmail.com', 22, 166)
    #person.present_me()
    #print("###############################")
    #print('nombre actualizado', person.get_first_name())
    #person.present_me()
    student = Student('livi ' , 'mercado','memlhfg90778', 'livi@hotmail.com', 22, 166)
    student.present_me()
    student.student_info()

    main()    


