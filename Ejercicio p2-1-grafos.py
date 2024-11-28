class GrafoUniverso:
    def __init__(self):
        self.planetas = {}  # Diccionario para almacenar los nodos y sus conexiones

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

    def mostrar_universo(self):
        """Muestra los planetas y sus rutas."""
        print("Universo de Dragon Ball:")
        for planeta, conexiones in self.planetas.items():
            print(f"{planeta} -> {conexiones}")

    def encontrar_ruta(self, origen, destino):
        """Encuentra una ruta entre dos planetas utilizando BFS."""
        if origen not in self.planetas or destino not in self.planetas:
            print("Uno o ambos planetas no existen en el universo.")
            return None

        visitados = set()
        cola = [(origen, [origen])]  # (nodo_actual, ruta_actual)

        while cola:
            nodo_actual, ruta = cola.pop(0)
            if nodo_actual == destino:
                return ruta

            for vecino in self.planetas[nodo_actual]:
                if vecino not in visitados:
                    visitados.add(vecino)
                    cola.append((vecino, ruta + [vecino]))

        print(f"No hay ruta entre {origen} y {destino}.")
        return None


# Creación del universo de Dragon Ball
universo = GrafoUniverso()

# Agregar planetas
universo.agregar_planeta("Tierra")
universo.agregar_planeta("Namek")
universo.agregar_planeta("Vegeta")
universo.agregar_planeta("Kaiosama")

# Agregar rutas espaciales
universo.agregar_ruta("Tierra", "Namek", 5000)
universo.agregar_ruta("Tierra", "Vegeta", 7000)
universo.agregar_ruta("Vegeta", "Kaiosama", 3000)
universo.agregar_ruta("Namek", "Kaiosama", 4000)

# Mostrar el universo
universo.mostrar_universo()

# Encontrar una ruta entre planetas
ruta = universo.encontrar_ruta("Tierra", "Kaiosama")
print("\nRuta encontrada:", " -> ".join(ruta) if ruta else "No hay ruta.")

Universo de Dragon Ball: # type: ignore
Tierra -> {'Namek': 5000, 'Vegeta': 7000} # type: ignore
Namek -> {'Tierra': 5000, 'Kaiosama': 4000} # type: ignore
Vegeta -> {'Tierra': 7000, 'Kaiosama': 3000} # type: ignore
Kaiosama -> {'Vegeta': 3000, 'Namek': 4000} # type: ignore
Ruta encontrada: Tierra -> Namek -> Kaiosama # type: ignore
