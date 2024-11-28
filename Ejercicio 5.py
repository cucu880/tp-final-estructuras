import heapq

class ColaPrioridadCombate:
    def __init__(self):
        self.heap = []

    def agregar_personaje(self, personaje):
        heapq.heappush(self.heap, (-personaje.nivel_poder, personaje)) # Para convertir en Max-Heapq negamos el nivel de poder

    def obtener_personaje_mas_fuerte(self):
        if self.heap:
            return heapq.heappop(self.heap)[1]
        else:
            return None
