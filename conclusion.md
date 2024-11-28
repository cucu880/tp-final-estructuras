# Tp-Estructura-de-datos
Juego Dragon Ball

Punto 5: Cola de Prioridades y Heap Binaria (Unidad 5):

•	Implementa una cola de prioridades para gestionar los combates en un torneo. Los personajes con el mayor nivel de poder tendrán prioridad en los enfrentamientos.

Implementación de una cola de prioridades para gestionar combates:

Objetivo: Crear una cola de prioridades donde los personajes con mayor nivel de poder tengan prioridad en los enfrentamientos. Esto es útil para organizar torneos donde los personajes más fuertes combaten primero o se enfrentan en rondas avanzadas.

Conceptos clave: 

1.	Cola de Prioridades:

o	Es una estructura de datos donde cada elemento tiene una prioridad asociada.

o	Los elementos con mayor prioridad se procesan antes que los de menor prioridad.

o	En este caso, la prioridad será el nivel de poder del personaje.

2.	Heap Binaria:

o	Se utiliza para implementar eficientemente una cola de prioridades.

o	Un Max-Heap es un árbol binario donde el valor de cada nodo es mayor o igual al de sus hijos. El nodo raíz contiene el valor máximo (en este caso, el personaje más fuerte).

Explicación:

•	Importar heapq: Python proporciona el módulo heapq para gestionar heaps.

•	Negar la prioridad: Dado que heapq implementa un Min-Heap por defecto (prioriza valores menores), negamos el nivel de poder para simular un Max-Heap.

•	Inserción: Se usa heapq. heappush para insertar un personaje con su nivel de poder negado.

•	Extracción: heapq. heappop elimina y devuelve el personaje con mayor prioridad.

Puntos clave: 

•	Inserción en O(log n): La operación de insertar en un heap binario es eficiente, incluso con un gran número de personajes.

•	Extracción en O(log n): Obtener el personaje más fuerte (prioridad máxima) también es eficiente.

•	Orden de Enfrentamientos: La estructura garantiza que los personajes más fuertes combatan primero.

Aplicación en torneos: 

•	Rondas de Combate: Se puede usar la cola de prioridades para organizar rondas donde los personajes más fuertes se enfrentan primero o avanzan más rápidamente.

•	 Simulación de Batallas: Después de cada combate, el ganador podría volver a insertarse con un nivel de poder ajustado (por ejemplo, aumentado por experiencia de combate).

Teoría:

Cola de prioridad implementada en el juego:

Las colas de prioridad son estructuras de datos muy útiles cuando necesitamos manejar elementos según su prioridad de forma que siempre podamos acceder al de mayor prioridad. En el contexto de nuestro juego de Dragon Ball, donde los personajes se enfrentan en batallas, podemos utilizar una cola de prioridad para asegurarnos de que los personajes con los niveles de poder más altos sean los primeros en ser elegidos para combatir. Esto hace que los enfrentamientos sean más equilibrados, ya que los personajes más fuertes tienen la oportunidad de luchar primero.

Estructura de datos: Heap binario.

Para implementar una cola de prioridades en Python, utilizamos un Heap Binario que se encuentra en la biblioteca heapq, esto nos permite gestionar estos heaps de forma una mejor manera. Por defecto, heapq implementa un Min-Heap, pero también podemos utilizarlo para crear un Max-Heap haciendo ajustes en el código.

•	Max-Heap: El valor máximo (personaje con mayor nivel de poder) siempre está en la raíz.

•	Min-Heap: El valor mínimo siempre está en la raíz.
Para nuestro juego, utilizaremos un Max-Heap, ya que queremos priorizar a los personajes más fuertes.
Operaciones: 

•	Insertar un personaje (push):

o	Agrega un nuevo elemento en la posición correcta según su nivel de prioridad (poder) y se posiciona en la raíz

o	Complejidad: O(log n) (el tiempo para insertar un personaje crece logarítmicamente con la cantidad de personajes).

•	Extraer al personaje más fuerte (pop):

o	Se elimina y devuelve el elemento con la máxima prioridad (raíz del heap).

o	Complejidad: O(log n) (La cantidad de comparaciones necesarias es proporcional a la altura del árbol, que es logarítmica).

•	Consultar al personaje más fuerte (peek):

o	Devuelve el personaje más fuerte sin eliminarlo.

o	Complejidad: O (1)O(1)O(1).

Para un juego de Dragon Ball, interesa utilizar un Max-Heap, ya que queremos priorizar a los personajes más fuertes.

•	Consultar al personaje más fuerte (peek):

o	Se obtiene el elemento de máxima prioridad sin eliminarlo.

o	Complejidad: O (1)O(1)O(1).


Conclusión:

Luego de concluir con todos los pasos del trabajo practico y haber desarrollado un juego ambientado en el universo de Dragon Ball, llegamos a la conclusión que, para construir un sistema funcional y además eficiente, es importante elegir adecuadamente las estructuras de datos adecuadas para cada parte del juego. Estas estructuras son las que organizan la información y optimizan todas las operaciones que queremos realizar. 
Para organizar la base del juego, utilizamos clases para representar los personajes y las habilidades de una forma más clara. Esto también ayudo a la creación de batallas y la evolución de los personajes.
Utilizamos arboles binarios para poder organizar a los personajes según su nivel de poder, lo que nos permitió búsquedas de inserción rápida para poder encontrar a los jugadores mas fuerte de un amanera más rápida. También utilizamos grafos para que los personajes viajen entre planetas.
Para los combates implementamos una cola de prioridad, esto nos aseguró que los personajes más fuertes jueguen primero. Por último, el ordenamiento topológico nos ayudó a que se desbloqueen las habilidades de los jugadores en el orden indicado.
Cada herramienta que usamos tuvo un propósito, no solo optimizando el rendimiento, sino que también a crear un juego entretenido para el usuario. Estas estructuras son esenciales para transformar ideas complejas en un juego que pueda ser funcional.






