## UT0 Entrega 4.1

Para la solución se optó por dividir el problema en dos búsquedas.
La primera búsqueda consta de dada una configuración de un solitario: cantidad de columnas, y cantidad de cartas en cada columna, encontrar un posible estado inicial de juego.

La segunda búsqueda consta de dado un solitiario,con su estado inicial, encontrar la secuencia de movimientos que lleven a su solución.

### Primera búsqueda, generar solitiario:

**Representación**: una lista de C listas en la cual cada sublista está compuesta por números enteros positivos comprendidos entre 1 y 13. 

**Estado inicial**: Permutación al azar de la estructura anterior

**Función sucesor**: Permutación de la mesa de cartas
Test objetivo: Existe una secuencia que permite ganar en el solitario (la búsqueda de dicha solución se hace mediante la segunda búsqueda, dicatada debajo)

**Estrategia de búsqueda**: Búsqueda aleatoria

**Consideraciones**

* C = cantidad de montones en la mesa
* L = lista de enteros positivos en la cual cada posición de la misma hace referencia al montón de cartas comenzando de izquierda a derecha. Ejemplo:  L = {5, 8, 6}.
* El primer montón de izquierda a derecha tiene 5 cartas
* El segundo montón de izquierda a derecha tiene 8 cartas
* El tercer montón de izquierda a derecha tiene 6 cartas
* M = {1, 2, 3, 4, 5, …, 13}

### Segunda búsqueda, resolver solitiario:

**Representación**: lista de enteros positivos comprendidos entre 1 y 13 en la cual cada elemento i de la misma cumple con: i – 1 < i < i + 1 en caso de que la posición de i no sea la primera de la lista.

**Estado inicial**: lista vacía.

**Función sucesor**:
- Si existe una carta en la mesa que sea adyacente a la carta dada vuelta, agregarla a la lista.
- En caso contrario, agregar a la lista una carta del mazo.

**Test objetivo**: la mesa está vacía y el mazo tiene al menos una carta.
Estrategia de búsqueda: Búsqueda en amplitud

### Ejecución de la implementación:

```bash
# Esto genera un solitario de 4 columnas,
# con 3, 2, y 4 cartas en cada columna respectivamente
$ python UTO_Entrega4.1.py 3,2,4

#OUTPUT
#Cartas en stack: ['2', 'Q', '4', '2', 'J', '9', '3', 'K', 'Q', 'K', '5', '5', 'J', '8', '10', '4', '3', 'Q', '8', '8', '9', '9', '10', 'A', '7', 'J', '10', 'A', '7', 'K', '2', '4', 'A', '3', '4', 'K', '3', 'A', '8', 'J', '7', 'Q', '10']
#Cartas en columnas: [['5', '6', '2'], ['9', '7'], ['6', '6', '6', '5']]