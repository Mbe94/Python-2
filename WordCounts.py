pip install pandas
!pip install pandas

import pandas as pd

# Texto inicial
text = """
El segundo encuentro multipartidario e interinstitucional, convocado por el Tribunal Supremo Electoral (TSE), expresó este lunes su pleno respaldo a la realización de las elecciones judiciales conjuntas el próximo 15 de diciembre y rechazó la polémica sentencia constitucional que puso en duda dicho proceso.
...
"""

# Limpiar el texto
text = text.lower()
for char in ".,;:!?":
    text = text.replace(char, "")

# Dividir el texto en palabras
words = text.split()

# Contar la frecuencia de cada palabra
word_freq = {word: words.count(word) for word in words}

# Lista de palabras a omitir
stop_words = {'el', 'la', 'de', 'las', 'y', 'en', 'del'}

# Filtrar el diccionario
filtered_word_freq = {word: freq for word, freq in word_freq.items() if word not in stop_words and freq > 1}

# Convertir a DataFrame y mostrar la tabla
df = pd.DataFrame(list(filtered_word_freq.items()), columns=['Palabra', 'Frecuencia'])
df = df.sort_values(by='Frecuencia', ascending=False)  # Ordenar por frecuencia

print("Tabla de palabras y frecuencias:")
print(df)