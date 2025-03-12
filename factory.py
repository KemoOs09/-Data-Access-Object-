from dao_interface import UsuarioDAO
from dao_sqlite import UsuarioDAOSQLite


class UsuarioDAOFactory:
    @staticmethod
    def get_dao(tipo: str = "sqlite", **kwargs) -> UsuarioDAO:
        if tipo == "sqlite":
            db_path = kwargs.get("db_path", "usuarios.db")
            return UsuarioDAOSQLite(db_path)
        # Podrían agregarse otras implementaciones (MySQL, PostgreSQL, etc.)
        raise ValueError(f"Tipo de DAO no soportado: {tipo}")