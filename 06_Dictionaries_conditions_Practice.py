# Ejercicio 1: Filtrar números pares en un diccionario
# Ejercicio: Dado un diccionario con números como valores, crea uno nuevo que solo contenga las claves cuyo valor sea par.

original_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
even_dict = {key: value for key, value in original_dict.items() if value % 2 == 0}
print(even_dict)
# Salida: {'b': 2, 'd': 4}

#--------------------------------------------------------------------------------

# Ejercicio 2: Asignar categorías según valores
# Ejercicio: Dado un diccionario con nombres y calificaciones, crea uno nuevo donde los valores sean "Aprobado" si la calificación es mayor o igual a 50, y "Reprobado" si es menor.

grades = {'Alice': 45, 'Bob': 67, 'Charlie': 39, 'Diana': 78}
status_dict = {name: 'Aprobado' if grade >= 50 else 'Reprobado' for name, grade in grades.items()}
print(status_dict)
# Salida: {'Alice': 'Reprobado', 'Bob': 'Aprobado', 'Charlie': 'Reprobado', 'Diana': 'Aprobado'}

#--------------------------------------------------------------------------------

# Filtrar un diccionario
# Ejercicio: De un diccionario, crea uno nuevo que solo contenga los elementos con valores mayores que 10.

original_dict = {'a': 5, 'b': 15, 'c': 25, 'd': 8}
filtered_dict = {key: value for key, value in original_dict.items() if value > 10}
print(filtered_dict)
# Salida: {'b': 15, 'c': 25}

#--------------------------------------------------------------------------------

