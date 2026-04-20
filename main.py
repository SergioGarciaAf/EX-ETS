from personajes import Jugador,Aldeano,lobo,Vidente
from logica import VICTORIAALDEANOS,VICTORIALOBOS,gestorPartida

# if __name__ == "__main__":
juego=gestorPartida()
juego.anadirJugador("Nacho", "lobo")
juego.anadirJugador("Elena", "vidente")
juego.anadirJugador("Carlos","aldeano")
print(juego.jugadores[0].AccionNocturna(juego.jugadores[2]))
print(juego.ComprobarVictoria())    