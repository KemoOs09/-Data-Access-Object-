from modelo import Usuario
from factory import UsuarioDAOFactory
import os
import time

def main():
    # Verificar si el archivo de base de datos existe
    if os.path.exists("ejemplo.db"):
        # Opción 1: Borrar la base de datos si existe
        os.remove("ejemplo.db")
        print("Base de datos anterior eliminada.")
    
    # Crear una instancia del DAO a través de la factory
    dao = UsuarioDAOFactory.get_dao(db_path="ejemplo.db")
    
    # Crear usuarios con correos únicos (agregando timestamp)
    timestamp = int(time.time())
    usuario1 = Usuario(nombre="Hugo Osorio", email=f"HugoOS{timestamp}@ejemplo.com", edad=21)
    usuario2 = Usuario(nombre="Urielrey", email=f"Uriellax{timestamp}@ejemplo.com", edad=22)
    
    # Insertar usuarios
    id1 = dao.insertar(usuario1)
    id2 = dao.insertar(usuario2)
    print(f"Usuario 1 insertado con ID: {id1}")
    print(f"Usuario 2 insertado con ID: {id2}")
    
    # Obtener todos los usuarios
    print("\nListado de todos los usuarios:")
    for usuario in dao.obtener_todos():
        print(usuario)
    
    # Actualizar un usuario
    usuario_actualizar = dao.obtener_por_id(id1)
    if usuario_actualizar:
        usuario_actualizar.edad = 31
        dao.actualizar(usuario_actualizar)
        print(f"\nUsuario actualizado: {dao.obtener_por_id(id1)}")
    
    # Eliminar un usuario
    if dao.eliminar(id2):
        print(f"\nUsuario con ID {id2} eliminado correctamente")
    
    # Mostrar usuarios restantes
    print("\nUsuarios restantes:")
    for usuario in dao.obtener_todos():
        print(usuario)


if __name__ == "__main__":
    main()