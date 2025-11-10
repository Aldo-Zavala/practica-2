# Método de ordenamiento Radix Sort

def counting_sort(lista, exp):
    n = len(lista)
    salida = [0] * n  # Lista de salida ordenada según el dígito actual
    conteo = [0] * 10  # Contador para los dígitos (0 al 9)
    
    # Contamos cuántos elementos tienen cada dígito en la posición actual
    for i in range(n):
        indice = (lista[i] // exp) % 10
        conteo[indice] += 1
    
    # Convertimos conteo[i] para que contenga la posición real en la salida
    for i in range(1, 10):
        conteo[i] += conteo[i - 1]
    
    # Construimos la lista de salida (de derecha a izquierda para estabilidad)
    i = n - 1
    while i >= 0:
        indice = (lista[i] // exp) % 10
        salida[conteo[indice] - 1] = lista[i]
        conteo[indice] -= 1
        i -= 1
    
    # Copiamos los elementos ordenados en la lista original
    for i in range(n):
        lista[i] = salida[i]


def radix_sort(lista):
    # Encontramos el número más grande para saber cuántos dígitos tiene
    maximo = max(lista)
    exp = 1  # exp = 1 representa unidades, 10 decenas, 100 centenas, etc.
    
    # Aplicamos counting sort para cada dígito
    while maximo // exp > 0:
        counting_sort(lista, exp)
        exp *= 10  # Pasamos al siguiente dígito


# Ejemplo de uso
numeros = [170, 45, 75, 90, 802, 24, 2, 66]
print("Lista original:", numeros)
radix_sort(numeros)
print("Lista ordenada:", numeros)
