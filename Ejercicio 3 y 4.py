class Habilidad:
    def __init__(self, nombre):
        self.nombre = nombre
        self.mejoras = []  #ramas

    def agregar_mejora(self, mejora):
        self.mejoras.append(mejora)

    def __str__(self):
        return self.nombre
class NodoHabilidad:
    def __init__(self, habilidad):
        self.habilidad = habilidad
        self.mejoras = []  #nodos de mejoras

    def agregar_mejora(self, nodo_mejora):
        self.mejoras.append(nodo_mejora)


class ArbolHabilidades:
    def __init__(self):
        self.raiz = None

    def insertar(self, habilidad):
        if not self.raiz:
            self.raiz = NodoHabilidad(habilidad)
        else:
            self._insertar_recursivo(self.raiz, habilidad)

    def _insertar_recursivo(self, nodo, habilidad):
           for mejora in nodo.mejoras:
            if mejora.habilidad.nombre == habilidad.nombre:
                return  # si ya existe no se inserta

           nodo.agregar_mejora(NodoHabilidad(habilidad))

    def mostrar(self):
        if self.raiz:
            self._mostrar(self.raiz, 0)

    def _mostrar(self, nodo, nivel):
        print(f"{'  ' * nivel}Habilidad: {nodo.habilidad.nombre}")
        for mejora in nodo.mejoras:
            self._mostrar(mejora, nivel + 1)
class Personaje:
    def __init__(self, nombre, nivel_poder):
        self.nombre = nombre
        self.nivel_poder = nivel_poder
        self.arbol_habilidades = ArbolHabilidades()
    #punto 4 habilidades
    def agregar_habilidad(self, habilidad):
        self.arbol_habilidades.insertar(habilidad)

    def mostrar_habilidades(self):
        self.arbol_habilidades.mostrar()
 

class NodoBinario:
    def __init__(self, personaje):
        self.personaje = personaje
        self.izquierda = None
        self.derecha = None

class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def insertar(self, personaje):
        if not self.raiz:
            self.raiz = NodoBinario(personaje)
        else:
            self._insertar_recursivo(self.raiz, personaje)

    def _insertar_recursivo(self, nodo, personaje):
        if personaje.nivel_poder < nodo.personaje.nivel_poder:
            if nodo.izquierda is None:
                nodo.izquierda = NodoBinario(personaje)
            else:
                self._insertar_recursivo(nodo.izquierda, personaje)
        else:
            if nodo.derecha is None:
                nodo.derecha = NodoBinario(personaje)
            else:
                self._insertar_recursivo(nodo.derecha, personaje)

# el pj mas fuerte esta en el nodo mas a la derecha
    def buscar_mas_fuerte(self):
        if self.raiz is None:
            return None
        return self._buscar_mas_fuerte_recursivo(self.raiz)

    def _buscar_mas_fuerte_recursivo(self, nodo):
        if nodo.derecha:
            return self._buscar_mas_fuerte_recursivo(nodo.derecha)
        return nodo.personaje
    
# lista de personajes In-Order (ya que empieza desde la izquierda , iria del mas debil al mas fuerte)
    def mostrar(self):
        personajes = []
        self._mostrar_inorden(self.raiz, personajes)
        for personaje in personajes:
            print(f"Personaje Z!: {personaje.nombre}, nivel de poder: {personaje.nivel_poder}")

    def _mostrar_inorden(self, nodo, personajes):
        if nodo:
            self._mostrar_inorden(nodo.izquierda, personajes)  
            personajes.append(nodo.personaje)  
            self._mostrar_inorden(nodo.derecha, personajes)  


#arbol    
arbol = ArbolBinario()

#crear personaje
goku = Personaje("Goku", 18000)
vegeta = Personaje("Vegeta", 17500)
Broly = Personaje("Broly", 20000)
Jiren = Personaje("Jiren", 21000)

#insertar en el arbol
arbol.insertar(goku)
arbol.insertar(vegeta)
arbol.insertar(Broly)
arbol.insertar(Jiren)
#buscar el pj mas fuerte
personaje_mas_fuerte = arbol.buscar_mas_fuerte()

if personaje_mas_fuerte:
    print(f"el pj mas fuerte es {personaje_mas_fuerte.nombre} con un nivel de poder de {personaje_mas_fuerte.nivel_poder}.")
else:
    print("el arbol esta vacio")

#mostrar todos los pj
arbol.mostrar()

#habilidades
kamehameha = Habilidad("Kamehameha")
kamehameha_x10 = Habilidad("Kamehameha x10")
kamehameha_x100 = Habilidad("Kamehameha x100")

#mejoras de habilidades
kamehameha.agregar_mejora(kamehameha_x10)
kamehameha_x10.agregar_mejora(kamehameha_x100)

#add habilidades a Goku ej
goku.agregar_habilidad(kamehameha)

# Mostrar habilidades de Goku
print(f"habilidades de {goku.nombre}:")
goku.mostrar_habilidades()

