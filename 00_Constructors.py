#Estos son herramientas muy prácticas para manipular datos de manera eficiente y son especialmente útiles en comprensiones:

#-----------------------------------------------------------------------------------------
    
#range()
#¿Qué hace?: Genera una secuencia de números, que puede ser usada para iterar en bucles o comprensiones.

#Sintáxis
# range(start, stop, step)

#Ejemplo
numeros = [x for x in range(5)]  # [0, 1, 2, 3, 4]
print(numeros)

#-----------------------------------------------------------------------------------------

#zip()

# ¿Qué hace?: Combina elementos de múltiples iterables (listas, tuplas, etc.) en pares.

# Uso común: Crear diccionarios a partir de dos listas.

keys = ["nombre", "edad", "país"]
values = ["Ana", 25, "Bolivia"]
diccionario = {k: v for k, v in zip(keys, values)}  # {'nombre': 'Ana', 'edad': 25, 'país': 'Bolivia'}
print(diccionario)

#-----------------------------------------------------------------------------------------

#enumerate()

# ¿Qué hace?: Agrega un índice a los elementos de un iterable.

# Uso común: Iterar sobre listas mientras rastreas el índice.

frutas = ["manzana", "pera", "uva"]
indices = {i: fruta for i, fruta in enumerate(frutas)}  # {0: 'manzana', 1: 'pera', 2: 'uva'}

#-----------------------------------------------------------------------------------------

#dict.items()

# ¿Qué hace?: Devuelve pares clave-valor de un diccionario como una lista de tuplas.

# Uso común: Procesar elementos de un diccionario.

diccionario = {"a": 1, "b": 2, "c": 3}
cuadrados = {k: v**2 for k, v in diccionario.items()}  # {'a': 1, 'b': 4, 'c': 9}
print (cuadrados)

#-----------------------------------------------------------------------------------------

#sorted()

# ¿Qué hace?: Devuelve una lista ordenada a partir de cualquier iterable.

# Uso común: Ordenar elementos de una lista, conjunto o diccionario.

numeros = [3, 1, 4, 1, 5]
ordenados = [x for x in sorted(numeros)]  # [1, 1, 3, 4, 5]
print(ordenados)