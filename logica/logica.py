from constantes import VICTORIALOBOS
from constantes import VICTORIAALDEANOS
from personajes.jugador import Jugador
class gestorPartida:  
    def __init__(self):
        self.jugadores =[]

    def anadirJugador(self, nombre, type):  
        self.jugadores.append(Jugador(nombre,type)) 
        
    def VotacionDia(self, NombreVotado):
        for j in self.jugadores:
            if j.Nombre == NombreVotado:
                if j.esta_vivo:
                    j.esta_vivo=False
                    return "El pueblo ha linchado a " + NombreVotado + " en la hoguera."
        return "Nadie fue linchado."    
    

    def ComprobarVictoria(self):  
        
        list = sum(1 for j in self.jugadores if j.rol == "lobo" and j.esta_vivo)
        dict = sum(1 for j in self.jugadores if j.rol != "lobo" and j.esta_vivo)
        
        if list >= dict:
            return VICTORIALOBOS
        elif list ==0:
            return VICTORIAALDEANOS
        return "La partida debe continuar..."


