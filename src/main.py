"""
Punto de entrada principal de la aplicación.
"""
class Usuario:
    """Clase para representar a un estudiante"""
 
    def __init__(self, nombre, edad, carrera):
        self.nombre = nombre
        self.edad = edad
        self.carrera = carrera
        self.materias = []
        self.actividades = []
        self.objetivos = []
 
    def agregar_materia(self, materia):
        for m in self.materias:
            if m.nombre.lower() == materia.nombre.lower():
                print(f"  ⚠ La materia '{materia.nombre}' ya está registrada.")
                return
        self.materias.append(materia)
        print(f"  ✓ Materia '{materia.nombre}' agregada exitosamente.")
 
    def agregar_actividad(self, actividad):
        self.actividades.append(actividad)
        print(f"  ✓ Actividad registrada: {actividad.descripcion} ({actividad.duracion_min} min)")
 
    def agregar_objetivo(self, objetivo):
        self.objetivos.append(objetivo)
        print(f"  ✓ Objetivo registrado: {objetivo.descripcion}")
 
    def mostrar_info(self):
        print(f"\n{'='*40}")
        print(f"  USUARIO: {self.nombre}")
        print(f"  Edad: {self.edad} años")
        print(f"  Carrera: {self.carrera}")
        print(f"  Materias registradas: {len(self.materias)}")
        print(f"  Actividades registradas: {len(self.actividades)}")
        print(f"{'='*40}")
 
    def __str__(self):
        return f"Usuario({self.nombre}, {self.carrera})"

def main():
    print("Proyecto POO - Iniciado")


if __name__ == "__main__":
    main()
