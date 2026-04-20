from jugador import Jugador
class Aldeano(Jugador):
    rol = "aldeano"

    def _ejecutar_accion(self, objetivo=None):
        return f"El aldeano {self.nombre} duerme profundamente."