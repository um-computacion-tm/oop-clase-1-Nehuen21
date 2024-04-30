import unittest
class Profesor:
    def __init__(self, nombre, cargo, legajo,antiguedad):
        self.__nombre__ = nombre
        self.__cargo__ = cargo
        self.__legajo__ = legajo
        self.__antiguedad__ = antiguedad

    def obtener_nombre(self):
        return self.__nombre__

    def obtener_cargo(self):
        return self.__cargo__

    def obtener_legajo(self):
        return self.__legajo__
    
    def obtener_antiguedad(self):
        return self.__antiguedad__
#-------------------------------------------------------------------------------------------------------------------------------   
class Alumno :
    def __init__(self,nombre,legajo,mail):
        self.__nombre__ = nombre
        self.__legajo__ = legajo
        self.__mail__ = mail

    def obtener_alumnos(self):
        return self.obtener_alumnos

# -----------------------------------------------------------------------------------------------------------------------------
class Materia:
    def __init__(self, nombre, profesores,alumnos:list[Alumno]):
        self.__nombre__ = nombre
        self.__profesores__ = profesores
        self.__alumnos__ = alumnos

    def obtener_profesores(self):
        return self.__profesores__

    def cambiar_nombre(self, nombre):
        self.__nombre__ = nombre

    def obtener_alumnos(self):
        return self.__alumnos__
#---------------------------------------------------------------------------------------------------------------------------
class TestClases(unittest.TestCase):
    def test_constructor_profesor(self):
        profesor1 = Profesor("Mariano Kloss", "Docente", 123,"3 años")
        profesor2 = Profesor("Adriana", "Pacheco", 456,"1 año")
        materia = Materia("Matemáticas", [profesor1, profesor2], [])

        self.assertEqual(materia.__nombre__, "Matemáticas")
        self.assertEqual(materia.__profesores__, [profesor1, profesor2])
        self.assertEqual(materia.__alumnos__, [])


    def test_constructor_materia(self):
        nombre = "Organizacion"
        profesores = "Mariano Kloss"
        alumno1 = Alumno("Facu corvalan", "62012",  "f.lucero")
        alumno2 = Alumno("Nazareno", "62127",  "N.Parodi")
        alumnos = [alumno1,alumno2]
        materia = Materia(nombre, profesores,alumnos)
        self.assertEqual(materia.__nombre__, nombre)
        self.assertEqual(materia.__profesores__, profesores)
        self.assertEqual(materia.__alumnos__, alumnos)


    def test_obtener_profesores(self):
         profesor = Profesor("Mariano Kloss", "Docente", "123", 3)
         self.assertEqual(profesor.obtener_nombre(), "Mariano Kloss")
        
    def test_obtener_cargo(self):
         cargo = Profesor("Mariano Kloss", "Docente", "123", 3)
         self.assertEqual(cargo.obtener_cargo(), "Docente")

    def test_obtener_legajo(self):
         legajo = Profesor("Mariano Kloss", "docente", "123", 3)
         self.assertEqual(legajo.obtener_legajo(), "123")

    def test_obtener_antiguedad(self):
         antiguedad = Profesor("Mariano Kloss", "docente", "123", 3)
         self.assertEqual(antiguedad.obtener_antiguedad(), 3)

    def obtener_nombre_alumnos(self):
        alumno = Alumno("Nehuen Donozo" , "62325",  "n.donozo")
        self.assertEqual(alumno.obtener_nombre(), "Lucas")

    def test_obtener_alumnos(self):
        alumno1 = Alumno("Nehuen Donozo", "62325", "n.donozo")
        alumno2 = Alumno("Nazareno Parodi", "62127",  "n.parodi")
        alumno3 = Alumno("facu lucero",'42232',"t.lucero")
        alumnos = [alumno1,alumno2,alumno3]
        materia = Materia('Organizacion','',alumnos)
        self.assertEqual(materia.obtener_alumnos(),alumnos)



unittest.main()


    


