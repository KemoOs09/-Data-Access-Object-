import sqlite3
from typing import List, Optional
from modelo import Usuario
from dao_interface import UsuarioDAO

class UsuarioDAOSQLite(UsuarioDAO):
    def __init__(self, db_path: str):
        self.db_path = db_path
        self._crear_tabla()
    
    def _crear_tabla(self):
        """Crea la tabla de usuarios si no existe"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                edad INTEGER
            )
        ''')
        conn.commit()
        conn.close()
    
    def obtener_todos(self) -> List[Usuario]:
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT id, nombre, email, edad FROM usuarios")
        usuarios = []
        for fila in cursor.fetchall():
            usuario = Usuario(id=fila[0], nombre=fila[1], email=fila[2], edad=fila[3])
            usuarios.append(usuario)
        conn.close()
        return usuarios
    
    def obtener_por_id(self, id: int) -> Optional[Usuario]:
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT id, nombre, email, edad FROM usuarios WHERE id = ?", (id,))
        fila = cursor.fetchone()
        conn.close()
        
        if fila:
            return Usuario(id=fila[0], nombre=fila[1], email=fila[2], edad=fila[3])
        return None
    
    def insertar(self, usuario: Usuario) -> int:
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO usuarios (nombre, email, edad) VALUES (?, ?, ?)",
            (usuario.nombre, usuario.email, usuario.edad)
        )
        usuario.id = cursor.lastrowid
        conn.commit()
        conn.close()
        return usuario.id
    
    def actualizar(self, usuario: Usuario) -> bool:
        if usuario.id is None:
            return False
        
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE usuarios SET nombre = ?, email = ?, edad = ? WHERE id = ?",
            (usuario.nombre, usuario.email, usuario.edad, usuario.id)
        )
        exito = cursor.rowcount > 0
        conn.commit()
        conn.close()
        return exito
    
    def eliminar(self, id: int) -> bool:
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM usuarios WHERE id = ?", (id,))
        exito = cursor.rowcount > 0
        conn.commit()
        conn.close()
        return exito