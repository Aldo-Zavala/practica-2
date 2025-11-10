import heapq  # Usamos una cola de prioridad para mezclar eficientemente

# Función de mezcla multivía balanceada
def balanced_multiway_merge(sublistas):
    # Usamos un heap para obtener siempre el menor elemento entre las sublistas
    heap = []
    resultado = []

    # Insertamos el primer elemento de cada sublista en el heap
    for i, sublista in enumerate(sublistas):
        if sublista:
            heapq.heappush(heap, (sublista[0], i, 0))  # (valor, índice sublista, índice elemento)
    
    # Mezclamos los elementos en orden
    while heap:
        valor, i_sublista, i_elem = heapq.heappop(heap)
        resultado.append(valor)
        
        # Si la sublista aún tiene elementos, insertamos el siguiente
        if i_elem + 1 < len(sublistas[i_sublista]):
            siguiente = sublistas[i_sublista][i_elem + 1]
            heapq.heappush(heap, (siguiente, i_sublista, i_elem + 1))
    
    return resultado


def balanced_multiway_merging_sort(lista, num_sublistas=3):
    n = len(lista)
    tam = (n + num_sublistas - 1) // num_sublistas  # Tamaño aproximado de cada sublista
    
    # Dividimos la lista en sublistas balanceadas
    sublistas = [lista[i:i + tam] for i in range(0, n, tam)]
    
    # Ordenamos cada sublista individualmente
    for i in range(len(sublistas)):
        sublistas[i].sort()
    
    # Mezclamos todas las sublistas
    lista_ordenada = balanced_multiway_merge(sublistas)
    return lista_ordenada


# Ejemplo de uso
numeros = [12, 3, 18, 7, 25, 1, 9, 14, 5, 20, 2]
print("Lista original:", numeros)
ordenada = balanced_multiway_merging_sort(numeros, num_sublistas=3)
print("Lista ordenada:", ordenada)
