1. Desarrollo de Clases e Interfaces
Clase Personaje
La clase Personaje encapsulará los siguientes atributos básicos:

nombre (str): Nombre del personaje.
nivel_de_poder (int): Poder actual del personaje.
habilidades (list): Lista de habilidades disponibles para el personaje.
raza (str): Raza del personaje, por ejemplo: Saiyajin, Namekuseijin, Terrícola.
Y métodos básicos como:

mostrar_estado(): Devuelve los datos actuales del personaje.
subir_de_nivel(): Incrementa el nivel de poder.
aprender_habilidad(habilidad): Agrega una nueva habilidad a la lista.
class Personaje:
    def __init__(self, nombre, nivel_de_poder, raza):
        self.nombre = nombre
        self.nivel_de_poder = nivel_de_poder
        self.habilidades = []
        self.raza = raza

    def mostrar_estado(self):
        return {
            "Nombre": self.nombre,
            "Nivel de Poder": self.nivel_de_poder,
            "Habilidades": self.habilidades,
            "Raza": self.raza,
        }

    def subir_de_nivel(self, incremento):
        self.nivel_de_poder += incremento
        print(f"{self.nombre} ha aumentado su nivel de poder a {self.nivel_de_poder}.")

    def aprender_habilidad(self, habilidad):
        if habilidad not in self.habilidades:
            self.habilidades.append(habilidad)
            print(f"{self.nombre} ha aprendido la habilidad: {habilidad}.")
        else:
            print(f"{self.nombre} ya conoce la habilidad {habilidad}.")
