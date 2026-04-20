from jugador import Jugador
class Vidente(Jugador):
    rol = "vidente"

    def _ejecutar_accion(self, objetivo):
        if objetivo:
            return f"La vidente {self.nombre} ve que {objetivo.nombre} es {objetivo.rol}."
        return f"La vidente {self.nombre} no eligió objetivo."