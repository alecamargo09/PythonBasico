from Enemigo import *

class Zombie(Enemigo):
    def _init_(self, puntos_energia=10, atque=1):
        super().__init__(tipo_enemigo="Zombie", puntos_energia=puntos_energia,)
    
    def habla(self):
        print("Hummm...")

    def propagar_enfermedad(self):
        print("El Zombie esta tratando depropagar la enfermedad")