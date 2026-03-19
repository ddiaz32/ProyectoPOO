"""
Punto de entrada principal de la aplicación.
"""
from datetime import datetime, date

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
    

class Materia:
    """Clase para representar una materia del estudiante"""
 
    def __init__(self, nombre, creditos=3, dificultad="media"):
        self.nombre = nombre
        self.creditos = creditos
        # dificultad puede ser: baja, media, alta
        self.dificultad = dificultad
 
    def __str__(self):
        return f"Materia({self.nombre}, {self.creditos} créditos, dificultad {self.dificultad})"
    

 
class ActividadEstudio:
    """Clase para representar una sesión de estudio"""
 
    def __init__(self, materia_nombre, descripcion, duracion_min, fecha=None):
        self.materia_nombre = materia_nombre
        self.descripcion = descripcion
        self.duracion_min = duracion_min
        # Si no se da fecha, se usa la actual
        if fecha is None:
            self.fecha = date.today()
        else:
            self.fecha = fecha
 
    def get_horas(self):
        """Retorna la duración en horas (con decimales)"""
        return round(self.duracion_min / 60, 2)
 
    def __str__(self):
        return (f"[{self.fecha}] {self.materia_nombre} - "
                f"{self.descripcion} ({self.duracion_min} min)")


class ObjetivoEstudio:
    """Clase para representar una meta de estudio"""
 
    def __init__(self, descripcion, horas_meta_semana, materia_nombre="General"):
        self.descripcion = descripcion
        self.horas_meta_semana = horas_meta_semana
        self.materia_nombre = materia_nombre
        self.cumplido = False
 
    def marcar_cumplido(self):
        self.cumplido = True
        print(f"  🎉 Objetivo '{self.descripcion}' marcado como cumplido!")
 
    def __str__(self):
        estado = "✓ Cumplido" if self.cumplido else "⏳ Pendiente"
        return f"Objetivo: {self.descripcion} | {self.horas_meta_semana}h/semana | {estado}"
    
class SistemaHabitos:
    """
    Clase principal que maneja todo el sistema.
    Aquí se guardan los usuarios y se hace el análisis.
    """
 
    def __init__(self):
        self.usuarios = []
 
    # ---------- RF1: Registrar usuario ----------
    def registrar_usuario(self, nombre, edad, carrera):
        """RF1 - Registrar un nuevo usuario"""
        # Verificar si ya existe
        for u in self.usuarios:
            if u.nombre.lower() == nombre.lower():
                print(f"  ⚠ El usuario '{nombre}' ya existe.")
                return None
        nuevo = Usuario(nombre, edad, carrera)
        self.usuarios.append(nuevo)
        print(f"\n  ✓ Usuario '{nombre}' registrado correctamente.")
        return nuevo
 
    def buscar_usuario(self, nombre):
        """Busca un usuario por nombre"""
        for u in self.usuarios:
            if u.nombre.lower() == nombre.lower():
                return u
        print(f"  ✗ Usuario '{nombre}' no encontrado.")
        return None
 
    # ---------- RF2: Registrar materia ----------
    def registrar_materia(self, nombre_usuario, nombre_materia,
                          creditos=3, dificultad="media"):
        """RF2 - Registrar una materia para un usuario"""
        usuario = self.buscar_usuario(nombre_usuario)
        if usuario is None:
            return
        nueva_materia = Materia(nombre_materia, creditos, dificultad)
        usuario.agregar_materia(nueva_materia)
 
    # ---------- RF3: Registrar actividad de estudio ----------
    def registrar_actividad(self, nombre_usuario, materia_nombre,
                            descripcion, duracion_min, fecha=None):
        """RF3 - Registrar una actividad de estudio"""
        usuario = self.buscar_usuario(nombre_usuario)
        if usuario is None:
            return
 
        # Verificar que la materia exista para ese usuario
        materia_valida = False
        for m in usuario.materias:
            if m.nombre.lower() == materia_nombre.lower():
                materia_valida = True
                break
 
        if not materia_valida:
            print(f"  ⚠ La materia '{materia_nombre}' no está registrada para {nombre_usuario}.")
            print(f"     Por favor registra primero la materia.")
            return
 
        actividad = ActividadEstudio(materia_nombre, descripcion, duracion_min, fecha)
        usuario.agregar_actividad(actividad)
 
    # ---------- RF4: Consultar historial ----------
    def consultar_historial(self, nombre_usuario, materia_filtro=None):
        """RF4 - Mostrar el historial de actividades de un usuario"""
        usuario = self.buscar_usuario(nombre_usuario)
        if usuario is None:
            return
 
        print(f"\n{'='*50}")
        print(f"  HISTORIAL DE ACTIVIDADES - {usuario.nombre.upper()}")
        print(f"{'='*50}")
 
        if len(usuario.actividades) == 0:
            print("  No hay actividades registradas aún.")
            return
 
        # Filtrar por materia si se especifica
        actividades_mostrar = usuario.actividades
        if materia_filtro:
            actividades_mostrar = [
                a for a in usuario.actividades
                if a.materia_nombre.lower() == materia_filtro.lower()
            ]
 
        if len(actividades_mostrar) == 0:
            print(f"  No hay actividades para la materia '{materia_filtro}'.")
            return
 
        total_minutos = 0
        for i, act in enumerate(actividades_mostrar, 1):
            print(f"  {i}. {act}")
            total_minutos += act.duracion_min
 
        print(f"\n  Total: {len(actividades_mostrar)} actividades | "
              f"{total_minutos} min ({round(total_minutos/60, 2)} horas)")
        print(f"{'='*50}")




        
def main():
    print("Proyecto POO - Iniciado")


if __name__ == "__main__":
    main()
