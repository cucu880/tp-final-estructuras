from collections import deque

# tecnicas
grafo = {
    "Técnica Base": [],  
    "Kaioken": ["Técnica Base"],  
    "Super Saiyajin": ["Técnica Base"],  
    "Kamehameha": ["Técnica Base"],  
    "Super Saiyajin 2": ["Super Saiyajin"],  
    "Kamehameha x10": ["Kamehameha"]  
}

def ordenamiento_topologico(grafo):
    # n de predecesores (entrada)
    grado_entrada = {}
    for nodo in grafo:
        grado_entrada[nodo] = 0 
    for nodos_dependientes in grafo.values():
        for dependiente in nodos_dependientes:
            grado_entrada[dependiente] += 1

    # cola con los nodos que no tienen predecesores
    cola = deque([nodo for nodo, grado in grado_entrada.items() if grado == 0])

    # ordenamiento topológico
    resultado = []
    while cola:
        nodo = cola.popleft()
        resultado.append(nodo)
        
        # reducir el grado de entrada de los nodos dependientes
        for dependiente in grafo[nodo]:
            grado_entrada[dependiente] -= 1
            if grado_entrada[dependiente] == 0:
                cola.append(dependiente)

    # Verificar el ordenamiento topológico
    if len(resultado) == len(grafo):
        return resultado
    else:
        raise ValueError("El grafo tiene un ciclo y no se puede ordenar topológicamente.")

# orden de entrenamiento
orden = ordenamiento_topologico(grafo)
print("El orden de entrenamiento es:")
print(" -> ".join(orden))