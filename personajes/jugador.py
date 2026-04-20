class Jugador:
    rol: str = "desconocido"

    def __init__(self, nombre):
        self.nombre = nombre
        self.esta_vivo = True

    def accion_nocturna(self, objetivo=None):
        if not self.esta_vivo:
            return f"{self.nombre} está muerto."
        return self._ejecutar_accion(objetivo)
