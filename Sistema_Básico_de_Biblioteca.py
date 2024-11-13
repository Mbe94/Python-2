#Sistema Básico de Biblioteca

#Este programa permitirá agregar títulos de libros a la colección, 
# eliminar libros y verificar si un libro está en la colección. 
# Usaremos un conjunto (set) para almacenar los títulos de libros, 
# ya que los conjuntos solo guardan elementos únicos, evitando duplicados automáticamente.

# Creamos un conjunto vacío para almacenar los libros
biblioteca = set()

# Agregamos libros manualmente
biblioteca.add("The Data Science Handbook: Advice and Insights from 25 Amazing Data Scientists")
biblioteca.add("Doing Data Science: Straight Talk from the Frontline")
biblioteca.add("Numsense! Data Science for the Layman: No Math Added")

# Imprimimos todos los libros en la colección
print("Libros en la colección:")
print(biblioteca)

# Eliminamos un libro manualmente
biblioteca.remove("Numsense! Data Science for the Layman: No Math Added")

# Imprimimos todos los libros después de la eliminación
print("Libros después de eliminar uno:")
print(biblioteca)

# Verificamos si un libro está en la colección
print("¿Está 'The Data Science Handbook: Advice and Insights from 25 Amazing Data Scientists' en la colección?")
print("The Data Science Handbook: Advice and Insights from 25 Amazing Data Scientists" in biblioteca)

print("¿Está 'Doing Data Science: Straight Talk from the Frontline' en la colección?")
print("Doing Data Science: Straight Talk from the Frontline" in biblioteca)