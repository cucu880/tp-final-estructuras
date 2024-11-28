import heapq

class Grafo:
    def __init__(self):
        self.grafo = {}  
    
    def agregar_planeta(self, planeta):
        if planeta not in self.grafo:
            self.grafo[planeta] = []
    
    def agregar_ruta(self, planeta1, planeta2, costo):
        """Agrega una ruta entre dos planetas con un costo (distancia o tiempo)."""
        self.grafo[planeta1].append((planeta2, costo))
        self.grafo[planeta2].append((planeta1, costo))  
    def mostrar_grafo(self):
        """Mostrar el grafo de planetas y sus rutas."""
        for planeta, rutas in self.grafo.items():
            print(f"{planeta} -> {', '.join([f'{destino} ({costo})' for destino, costo in rutas])}")

def dijkstra(grafo, inicio):
    distancias = {planeta: float('inf') for planeta in grafo.grafo}
    distancias[inicio] = 0
    
    # Cola de prioridad para explorar el grafo
    cola = [(0, inicio)]  # Tupla (distancia, nodo)
    
    while cola:
        distancia_actual, planeta_actual = heapq.heappop(cola)
        
        if distancia_actual > distancias[planeta_actual]:
            continue
        for vecino, costo in grafo.grafo[planeta_actual]:
            nueva_distancia = distancia_actual + costo
            if nueva_distancia < distancias[vecino]:
                distancias[vecino] = nueva_distancia
                heapq.heappush(cola, (nueva_distancia, vecino))
    
    return distancias

# grafo
universo = Grafo()

# Agregar planetas
universo.agregar_planeta("Tierra")
universo.agregar_planeta("Namek")
universo.agregar_planeta("Vegeta")
universo.agregar_planeta("Kamisama templo")
universo.agregar_planeta("Supreme Kaiosama planeta")

# Agregar rutas entre planetas con sus respectivos costos (distancia o tiempo de viaje)
universo.agregar_ruta("Tierra", "Namek", 3000)
universo.agregar_ruta("Tierra", "Vegeta", 2000)
universo.agregar_ruta("Namek", "Kamisama templo", 4000)
universo.agregar_ruta("Vegeta", "Kamisama templo", 1000)
universo.agregar_ruta("Kamisama templo", "Supreme Kaiosama planeta", 5000)

# Mostrar el grafo
universo.mostrar_grafo()

# Aplicar Dijkstra desde "Tierra"
distancias = dijkstra(universo, "Tierra")
print("\nDistancias mínimas desde Tierra:")
for planeta, distancia in distancias.items():
    print(f"Distancia desde Tierra a {planeta}: {distancia}")
