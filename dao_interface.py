from typing import List, Optional
from modelo import Usuario

class UsuarioDAO:
    def obtener_todos(self) -> List[Usuario]:
        pass
    
    def obtener_por_id(self, id: int) -> Optional[Usuario]:
        pass
    
    def insertar(self, usuario: Usuario) -> int:
        pass
    
    def actualizar(self, usuario: Usuario) -> bool:
        pass
    
    def eliminar(self, id: int) -> bool:
        pass