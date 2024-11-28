Punto 6. Análisis de Algoritmos (Unidad 6):
•	Analiza la eficiencia de los algoritmos utilizados para las batallas, la evolución de poder y la organización de los personajes. Discute la complejidad en términos de tiempo y espacio para cada estructura de datos.

•	Algoritmo recursivo para la evolución del poder
Este proceso que calcula la evolución del poder de un personaje utiliza multiplicadores asociados a transformaciones. Para calcular su poder en cada etapa, por ejemplo, un personaje como Goku quiere alcanzar nuevas transformaciones, desde el Kaioken hasta el Super Saiyajin, si queremos calcular su poder utilizamos un algoritmo recursivo. La complejidad temporal de este algoritmo es O(n), donde se multiplica el poder base por un factor específico en cada transformación, por lo que, si Goku pasa por n transformaciones, el algoritmo realizará n multiplicaciones.
•	Árbol binario de búsqueda para la organización de personajes 
Lo utilizamos para clasificar a los personajes según su nivel de poder, esta nos permite buscar e insertar personajes más rápido, con una complejidad promedio de O(log n), donde n es el número de personajes. Pero si el árbol esta desbalanceado (poderes similares o inserción en orden), podría se O(n).
•	Árbol general para el sistema de habilidades 
El árbol general se emplea para representar las habilidades de los personajes, cada nodo simboliza una técnica y sus mejoras (por ejemplo, el kamehameha). Si ya podemos acceder al nodo donde queremos insertar una habilidad, la operación es muy rápida O(1). Pero si queremos buscar un nodo específico, la complejidad es O(n). El recorrido completo del árbol también es lineal, O(n), porque cada nodo debe ser visitado. En términos de espacio, esta estructura ocupa O(n), siendo n la cantidad de habilidades. Una posible mejora sería usar un diccionario auxiliar para acelerar la búsqueda de habilidades específicas. 
•	Cola de prioridad para la gestión de combates 
En un torneo, los combates deben ser organizados de manera que los personajes más fuertes peleen primero. Por este motivo utilizamos la cola de prioridades basada en un Max-Heap. Para insertar un personaje o sacar al más fuerte toma O(log n), mientras que consultar al más fuerte (que siempre está en la cima) es casi instantáneo: O(1), porque siempre está en la raíz del heap. En cuanto al espacio, la cola de prioridad ocupa O(n), donde n es el número de personajes. 


