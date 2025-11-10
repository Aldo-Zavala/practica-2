# Método de ordenamiento QuickSort

def quicksort(lista):
    # Caso base: listas vacías o con un solo elemento ya están ordenadas
    if len(lista) <= 1:
        return lista
    
    # Elegimos el pivote (aquí el último elemento)
    pivote = lista[-1]
    
    # Dividimos la lista en dos: menores y mayores al pivote
    menores = [x for x in lista[:-1] if x <= pivote]
    mayores = [x for x in lista[:-1] if x > pivote]
    
    # Llamada recursiva
    return quicksort(menores) + [pivote] + quicksort(mayores)


# Ejemplo de uso
numeros = [8, 3, 5, 1, 9, 2]
print("Lista original:", numeros)
ordenada = quicksort(numeros)
print("Lista ordenada:", ordenada)
