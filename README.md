#Ejemplo DAO

Este programa implementa un sistema básico de gestión de usuarios utilizando el patrón de diseño DAO (Data Access Object). El patrón DAO es una estrategia de diseño que permite separar la lógica de acceso a datos de la lógica de negocio, lo que facilita el mantenimiento y la modificación del código, especialmente cuando se necesita cambiar la fuente de datos.


#Estructura del Programa
El programa está organizado en cinco archivos principales:

modelo.py: Define la entidad Usuario
dao_interface.py: Define la interfaz DAO con métodos abstractos
dao_sqlite.py: Implementa la interfaz DAO para bases de datos SQLite
factory.py: Crea instancias concretas de DAOs
main.py: Punto de entrada del programa con ejemplos de uso

#Flujo de Operación

El programa crea una instancia DAO a través de la factory
Define dos usuarios de ejemplo
Inserta los usuarios en la base de datos
Recupera y muestra todos los usuarios
Actualiza la edad de un usuario
Elimina un usuario
Muestra los usuarios restantes

#Base de Datos
El sistema crea automáticamente una base de datos SQLite llamada "ejemplo.db" con una estructura para almacenar:

ID del usuario (clave primaria, autoincremental)
Nombre (texto, obligatorio)
Email (texto, único, obligatorio)
Edad (entero)
