from jugador import Jugador
class Lobo(Jugador):
    rol = "lobo"

    def _ejecutar_accion(self, objetivo):
        if objetivo and objetivo.esta_vivo:
            objetivo.esta_vivo = False
            return f"El lobo {self.nombre} ha eliminado a {objetivo.nombre}."
        return f"El lobo {self.nombre} no eligió un objetivo válido."