def selection_sort(lista):
    n = len(lista)
    
    # Recorremos toda la lista
    for i in range(n - 1):
        # Suponemos que el menor está en la posición i
        indice_menor = i
        
        # Buscamos el elemento menor en el resto de la lista
        for j in range(i + 1, n):
            if lista[j] < lista[indice_menor]:
                indice_menor = j
        
        # Intercambiamos los elementos
        lista[i], lista[indice_menor] = lista[indice_menor], lista[i]
    
    return lista


# Ejemplo de uso
numeros = [8, 3, 5, 1, 9, 2]
print("Lista original:", numeros)
ordenada = selection_sort(numeros)
print("Lista ordenada:", ordenada)