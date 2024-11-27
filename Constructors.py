#Estos son herramientas muy prácticas para manipular datos de manera eficiente y son especialmente útiles en comprensiones:

#-----------------------------------------------------------------------------------------

#range()
#¿Qué hace?: Genera una secuencia de números, que puede ser usada para iterar en bucles o comprensiones.

#Sintáxis
# range(start, stop, step)

#Ejemplo
numeros = [x for x in range(5)]  # [0, 1, 2, 3, 4]

#-----------------------------------------------------------------------------------------

#zip()

# ¿Qué hace?: Combina elementos de múltiples iterables (listas, tuplas, etc.) en pares.

# Uso común: Crear diccionarios a partir de dos listas.

keys = ["nombre", "edad", "país"]
values = ["Ana", 25, "Bolivia"]
diccionario = {k: v for k, v in zip(keys, values)}  # {'nombre': 'Ana', 'edad': 25, 'país': 'Bolivia'}