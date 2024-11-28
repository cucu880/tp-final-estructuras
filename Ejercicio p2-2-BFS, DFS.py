class GrafoUniverso:
    def __init__(self):
        self.planetas = {}  # Diccionario para almacenar nodos y conexiones

    def agregar_planeta(self, planeta):
        """Agrega un planeta como nodo al grafo."""
        if planeta not in self.planetas:
            self.planetas[planeta] = {}
            print(f"Planeta {planeta} agregado al universo.")
        else:
            print(f"El planeta {planeta} ya existe en el universo.")

    def agregar_ruta(self, origen, destino, distancia):
        """Agrega una ruta entre dos planetas con una distancia."""
        if origen in self.planetas and destino in self.planetas:
            self.planetas[origen][destino] = distancia
            self.planetas[destino][origen] = distancia  # Grafo no dirigido
            print(f"Ruta agregada entre {origen} y {destino} con distancia {distancia}.")
        else:
            print("Uno o ambos planetas no existen en el universo.")

    def dfs(self, origen, objetivo, visitados=None, camino=None):
        """Algoritmo DFS para encontrar el camino entre planetas."""
        if visitados is None:
            visitados = set()
        if camino is None:
            camino = []

        visitados.add(origen)
        camino.append(origen)

        if origen == objetivo:
            return camino

        for vecino in self.planetas[origen]:
            if vecino not in visitados:
                resultado = self.dfs(vecino, objetivo, visitados, camino)
                if resultado:  # Si se encuentra el objetivo
                    return resultado

        camino.pop()  # Retroceder si no se encuentra el objetivo en este camino
        return None

    def bfs(self, origen, objetivo):
        """Algoritmo BFS para encontrar el camino más corto entre planetas."""
        visitados = set()
        cola = [(origen, [origen])]  # (nodo_actual, camino_actual)

        while cola:
            nodo_actual, camino = cola.pop(0)

            if nodo_actual == objetivo:
                return camino

            if nodo_actual not in visitados:
                visitados.add(nodo_actual)
                for vecino in self.planetas[nodo_actual]:
                    if vecino not in visitados:
                        cola.append((vecino, camino + [vecino]))

        return None


# Creación del universo de Dragon Ball
universo = GrafoUniverso()

# Agregar planetas
universo.agregar_planeta("Tierra")
universo.agregar_planeta("Namek")
universo.agregar_planeta("Vegeta")
universo.agregar_planeta("Kaiosama")
universo.agregar_planeta("Nuevo Namek")

# Agregar rutas espaciales
universo.agregar_ruta("Tierra", "Namek", 5000)
universo.agregar_ruta("Tierra", "Vegeta", 7000)
universo.agregar_ruta("Vegeta", "Kaiosama", 3000)
universo.agregar_ruta("Namek", "Kaiosama", 4000)
universo.agregar_ruta("Namek", "Nuevo Namek", 2000)

# Mostrar el universo
print("\nUniverso creado:")
universo.mostrar_universo()

# Buscar un personaje desaparecido en Nuevo Namek usando DFS
print("\nBúsqueda DFS desde Tierra a Nuevo Namek:")
camino_dfs = universo.dfs("Tierra", "Nuevo Namek")
print("Camino encontrado (DFS):", " -> ".join(camino_dfs) if camino_dfs else "No encontrado.")

# Buscar un personaje desaparecido en Nuevo Namek usando BFS
print("\nBúsqueda BFS desde Tierra a Nuevo Namek:")
camino_bfs = universo.bfs("Tierra", "Nuevo Namek")
print("Camino encontrado (BFS):", " -> ".join(camino_bfs) if camino_bfs else "No encontrado.")

Universo creado:
Tierra -> {'Namek': 5000, 'Vegeta': 7000}
Namek -> {'Tierra': 5000, 'Kaiosama': 4000, 'Nuevo Namek': 2000}
Vegeta -> {'Tierra': 7000, 'Kaiosama': 3000}
Kaiosama -> {'Vegeta': 3000, 'Namek': 4000}
Nuevo Namek -> {'Namek': 2000}

Búsqueda DFS desde Tierra a Nuevo Namek:
Camino encontrado (DFS): Tierra -> Namek -> Nuevo Namek

Búsqueda BFS desde Tierra a Nuevo Namek:
Camino encontrado (BFS): Tierra -> Namek -> Nuevo Namek
