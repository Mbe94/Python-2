# Sistema Básico de Biblioteca

# Este programa permitirá agregar títulos de libros a la colección, 
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

# Colecciones de libros
novedades = {'El Poder del Presente', 'Mindset: La Nueva Psicología del Éxito', 'Atomic Habits: Cómo crear hábitos buenos y romper los malos'}
recomendados = {'El Instituto', 'La Fórmula de la Felicidad', 'El Código del Universo'}

# Unión: Todos los libros en ambas colecciones
todos_libros = novedades.union(recomendados)
print("Todos los libros:", todos_libros)

# Intersección: Libros en común entre ambas colecciones
libros_comunes = novedades.intersection(recomendados)
print("Libros en ambas colecciones:", libros_comunes)

# Diferencia: Libros en 'Novedades' que no están en 'Recomendados'
solo_novedades = novedades.difference(recomendados)
print("Solo en Novedades:", solo_novedades)

# Diferencia Simétrica: Libros que están en una colección pero no en ambas
libros_unicos = novedades.symmetric_difference(recomendados)
print("Libros exclusivos de cada colección:", libros_unicos)

# Unión: Todos los libros en ambas colecciones
todos_libros = novedades.union(recomendados)
print("Todos los libros:", todos_libros)

# Unión: Todos los libros en ambas colecciones
todos_libros = biblioteca | novedades | recomendados
print("Todos los libros (Unión):", todos_libros)

# Intersección: Libros en común entre las colecciones
libros_comunes = biblioteca & novedades & recomendados
print("Libros en ambas colecciones (Intersección):", libros_comunes)

# Diferencia: Libros en 'Biblioteca' que no están en 'Novedades' ni en 'Recomendados'
solo_biblioteca = biblioteca - novedades - recomendados
print("Libros solo en Biblioteca (Diferencia):", solo_biblioteca)

# Diferencia Simétrica: Libros que están en una colección pero no en ambas
libros_unicos = biblioteca ^ novedades ^ recomendados
print("Libros exclusivos de cada colección (Diferencia Simétrica):", libros_unicos)