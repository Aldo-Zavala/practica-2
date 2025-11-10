# Método de ordenamiento Straight Merging (Mezcla Directa)

def merge(lista_izq, lista_der):
    resultado = []
    i = j = 0
    
    # Combinamos las dos listas ordenadas
    while i < len(lista_izq) and j < len(lista_der):
        if lista_izq[i] < lista_der[j]:
            resultado.append(lista_izq[i])
            i += 1
        else:
            resultado.append(lista_der[j])
            j += 1
    
    # Agregamos los elementos restantes
    resultado.extend(lista_izq[i:])
    resultado.extend(lista_der[j:])
    
    return resultado


def straight_merging_sort(lista):
    # Cada elemento comienza siendo una sublista
    sublistas = [[x] for x in lista]
    
    # Mientras haya más de una sublista, se van combinando
    while len(sublistas) > 1:
        nueva_lista = []
        
        # Mezclamos las sublistas de dos en dos
        for i in range(0, len(sublistas), 2):
            if i + 1 < len(sublistas):
                combinada = merge(sublistas[i], sublistas[i + 1])
                nueva_lista.append(combinada)
            else:
                nueva_lista.append(sublistas[i])
        
        sublistas = nueva_lista  # Repetimos hasta tener una sola lista
    
    return sublistas[0]


# Ejemplo de uso
numeros = [8, 3, 5, 1, 9, 2, 7, 4]
print("Lista original:", numeros)
ordenada = straight_merging_sort(numeros)
print("Lista ordenada:", ordenada)
