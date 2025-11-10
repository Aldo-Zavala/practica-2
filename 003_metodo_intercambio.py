def bubble_sort(lista):
    n = len(lista)
    
    # Recorremos toda la lista
    for i in range(n - 1):
        # En cada pasada, el elemento más grande "sube" al final
        for j in range(n - 1 - i):
            # Si el elemento actual es mayor que el siguiente, intercambiamos
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    
    return lista


# Ejemplo de uso
numeros = [8, 3, 5, 1, 9, 2]
print("Lista original:", numeros)
ordenada = bubble_sort(numeros)
print("Lista ordenada:", ordenada)