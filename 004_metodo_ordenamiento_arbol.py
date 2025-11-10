class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izq = None
        self.der = None

# Función para insertar un valor en el árbol binario
def insertar(raiz, valor):
    if raiz is None:
        return Nodo(valor)
    if valor < raiz.valor:
        raiz.izq = insertar(raiz.izq, valor)
    else:
        raiz.der = insertar(raiz.der, valor)
    return raiz

# Función para recorrer el árbol en orden (in-order traversal)
def recorrido_inorden(raiz, resultado):
    if raiz is not None:
        recorrido_inorden(raiz.izq, resultado)
        resultado.append(raiz.valor)
        recorrido_inorden(raiz.der, resultado)

# Función principal del método Tree Sort
def tree_sort(lista):
    raiz = None
    for valor in lista:
        raiz = insertar(raiz, valor)
    
    resultado = []
    recorrido_inorden(raiz, resultado)
    return resultado


# Ejemplo de uso
numeros = [8, 3, 5, 1, 9, 2]
print("Lista original:", numeros)
ordenada = tree_sort(numeros)
print("Lista ordenada:", ordenada)