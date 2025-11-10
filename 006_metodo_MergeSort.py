# Método de ordenamiento por mezcla (Merge Sort)

def merge_sort(lista):
    # Caso base: si la lista tiene 1 o 0 elementos, ya está ordenada
    if len(lista) <= 1:
        return lista
    
    # Dividimos la lista en dos mitades
    mitad = len(lista) // 2
    izquierda = lista[:mitad]
    derecha = lista[mitad:]
    
    # Ordenamos cada mitad recursivamente
    izquierda = merge_sort(izquierda)
    derecha = merge_sort(derecha)
    
    # Mezclamos las dos mitades ordenadas
    return mezclar(izquierda, derecha)


def mezclar(izquierda, derecha):
    resultado = []
    i = j = 0
    
    # Comparamos y unimos las dos mitades
    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] < derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1
    
    # Agregamos los elementos restantes (si los hay)
    resultado += izquierda[i:]
    resultado += derecha[j:]
    
    return resultado


# Ejemplo de uso
numeros = [8, 3, 5, 1, 9, 2]
print("Lista original:", numeros)
ordenada = merge_sort(numeros)
print("Lista ordenada:", ordenada)
