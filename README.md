# Curso de Python: Comprehensions, Funciones y Manejo de Errores

## El Zen de Python

El Zen de Python es una colección de 19 principios guía para escribir programas en Python. Estos principios fueron escritos por Tim Peters y están incluidos en el PEP 20 (Python Enhancement Proposal 20). Puedes acceder a ellos escribiendo "import this" en el intérprete de Python. Aquí están los principios:

- Bello es mejor que feo.
- Explícito es mejor que implícito.
- Simple es mejor que complejo.
- Complejo es mejor que complicado.
- Plano es mejor que anidado.
- Espaciado es mejor que denso.
- La legibilidad es importante.
- Los casos especiales no son lo suficientemente especiales como para romper las reglas.
- Sin embargo, lo práctico le gana a la pureza.
- Los errores nunca deberían pasar silenciosamente.
- A menos que se silencien explícitamente.
- Frente a la ambigüedad, evita la tentación de adivinar.
- Debería haber una, y preferiblemente solo una, manera obvia de hacerlo.
- A pesar de que esa manera no sea obvia a menos que seas holandés.
- Ahora es mejor que nunca.
- Aunque nunca es a menudo mejor que *ahora mismo*.
- Si la implementación es difícil de explicar, es una mala idea.
- Si la implementación es fácil de explicar, puede que sea una buena idea.
- Los espacios de nombres son una gran idea, ¡tengamos más de esos!

Estos principios enfatizan la importancia de la claridad, la simplicidad y la legibilidad en el código Python, y sirven como una guía filosófica para los desarrolladores de Python.

## Sets en Python

Los sets en Python son colecciones desordenadas de elementos únicos. Son útiles para eliminar duplicados y realizar operaciones de conjuntos como unión, intersección y diferencia.

### Características principales de los sets:

- Son mutables, pero solo pueden contener elementos inmutables.
- No mantienen un orden específico de los elementos.
- No permiten elementos duplicados.
- Son iterables.

### Creación de sets:

```python
# Usando llaves
mi_set = {1, 2, 3, 4, 5}

# Usando la función set()
otro_set = set([1, 2, 3, 3, 4, 5])  # Los duplicados se eliminan automáticamente

# Set vacío
set_vacio = set()
```

### Operaciones comunes con sets:

```python
# Añadir elementos
mi_set.add(6)

# Eliminar elementos
mi_set.remove(3)  # Lanza un error si el elemento no existe
mi_set.discard(3)  # No lanza error si el elemento no existe

# Operaciones de conjuntos
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union = set1 | set2  # {1, 2, 3, 4, 5}
interseccion = set1 & set2  # {3}
diferencia = set1 - set2  # {1, 2}
```

Los sets son una estructura de datos poderosa en Python, especialmente útiles cuando necesitas trabajar con colecciones de elementos únicos o realizar operaciones de conjuntos de manera eficiente.

### Modificando Sets

Los sets en Python ofrecen varios métodos para modificar su contenido. Aquí se presentan algunos de los más comunes:

```python
# Crear un set
mi_set = {1, 2, 3, 4, 5}

# Añadir un elemento
mi_set.add(6)

# Añadir múltiples elementos
mi_set.update([7, 8, 9])

# Eliminar un elemento específico
mi_set.remove(3)  # Lanza KeyError si el elemento no existe

# Eliminar un elemento si existe
mi_set.discard(10)  # No lanza error si el elemento no existe

# Eliminar y devolver un elemento arbitrario
elemento = mi_set.pop()

# Eliminar todos los elementos
mi_set.clear()

print(mi_set)  # Imprime set(), un conjunto vacío
```

Es importante recordar que, debido a la naturaleza no ordenada de los sets, métodos como pop() eliminarán un elemento arbitrario. Además, al ser mutables, los sets pueden ser modificados, pero solo pueden contener elementos inmutables.

## Operaciones con SETS

Los sets en Python permiten realizar diversas operaciones matemáticas de conjuntos. Estas operaciones son muy útiles para comparar y combinar diferentes conjuntos de datos. A continuación, se presentan algunas de las operaciones más comunes:

### Unión

La unión de dos sets incluye todos los elementos que están en cualquiera de los dos sets.

```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union = set1 | set2  # También se puede usar set1.union(set2)
print(union)  # Output: {1, 2, 3, 4, 5}
```

### Intersección

La intersección de dos sets incluye solo los elementos que están en ambos sets.

```python
interseccion = set1 & set2  # También se puede usar set1.intersection(set2)
print(interseccion)  # Output: {3}
```

### Diferencia

La diferencia entre dos sets incluye los elementos que están en el primer set pero no en el segundo.

```python
diferencia = set1 - set2  # También se puede usar set1.difference(set2)
print(diferencia)  # Output: {1, 2}
```

### Diferencia simétrica

La diferencia simétrica incluye elementos que están en cualquiera de los sets, pero no en ambos.

```python
diff_simetrica = set1 ^ set2  # También se puede usar set1.symmetric_difference(set2)
print(diff_simetrica)  # Output: {1, 2, 4, 5}
```

Estas operaciones son muy eficientes en Python y son especialmente útiles cuando se trabaja con grandes conjuntos de datos y se necesita realizar comparaciones o combinaciones rápidas.

## List Comprehension

List comprehension es una forma concisa y elegante de crear listas en Python. Permite crear nuevas listas basadas en listas existentes o cualquier otro iterable de una manera más compacta que usando bucles for tradicionales.

### Sintaxis básica:

```python
nueva_lista = [expresion for item in iterable if condicion]
```

Donde:

- **expresion:** Es el valor que se añadirá a la nueva lista.
- **item:** Es la variable que toma cada valor del iterable.
- **iterable:** Es la secuencia sobre la que se itera (lista, tupla, etc.).
- **condicion:** (Opcional) Filtro que determina qué elementos se incluyen.

### Ejemplos:

```python
# Lista de cuadrados
cuadrados = [x**2 for x in range(10)]
print(cuadrados)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Lista de números pares
pares = [x for x in range(20) if x % 2 == 0]
print(pares)  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# Convertir temperaturas de Celsius a Fahrenheit
celsius = [0, 10, 20, 30, 40]
fahrenheit = [(9/5)*temp + 32 for temp in celsius]
print(fahrenheit)  # [32.0, 50.0, 68.0, 86.0, 104.0]
```

Las list comprehensions son una característica poderosa de Python que puede hacer el código más legible y eficiente cuando se usa apropiadamente.

## Dictionary Comprehension

Dictionary comprehension es una técnica similar a list comprehension, pero se utiliza para crear diccionarios de manera concisa en Python. Permite generar diccionarios basados en iterables o en otros diccionarios de forma eficiente.

### Sintaxis básica:

```python
nuevo_dict = {clave_expr: valor_expr for item in iterable if condicion}
```

Donde:

- **clave_expr:** Es la expresión que genera la clave del diccionario.
- **valor_expr:** Es la expresión que genera el valor asociado a la clave.
- **item:** Es la variable que toma cada valor del iterable.
- **iterable:** Es la secuencia sobre la que se itera.
- **condicion:** (Opcional) Filtro que determina qué elementos se incluyen.

### Ejemplos:

```python
# Crear un diccionario de cuadrados
cuadrados = {x: x**2 for x in range(5)}
print(cuadrados)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Crear un diccionario con strings como claves
frutas = ['manzana', 'banana', 'cereza']
longitudes = {fruta: len(fruta) for fruta in frutas}
print(longitudes)  # {'manzana': 7, 'banana': 6, 'cereza': 6}

# Filtrar elementos en un diccionario
numeros = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
pares = {k: v for k, v in numeros.items() if v % 2 == 0}
print(pares)  # {'b': 2, 'd': 4}
```

Las dictionary comprehensions son una herramienta poderosa para crear y transformar diccionarios de manera eficiente y legible en Python.

### Uso de condiciones en Dictionary Comprehension

Las condiciones en dictionary comprehension permiten filtrar elementos basados en criterios específicos. Esto es útil para crear diccionarios selectivos a partir de datos existentes.

```python
# Ejemplo: Crear un diccionario de números impares y sus cuadrados
impares_cuadrados = {x: x**2 for x in range(10) if x % 2 != 0}
print(impares_cuadrados)  # {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}

# Ejemplo: Filtrar palabras por longitud
palabras = ['gato', 'perro', 'elefante', 'ratón', 'jirafa']
palabras_largas = {palabra: len(palabra) for palabra in palabras if len(palabra) > 4}
print(palabras_largas)  # {'elefante': 8, 'jirafa': 6}
```

Las condiciones en dictionary comprehension ofrecen una forma elegante de crear diccionarios filtrados, mejorando la legibilidad y eficiencia del código.

## Lists vs. Tuples vs. Sets

En Python, las listas, tuplas y sets son estructuras de datos importantes, cada una con sus propias características y usos. Aquí se presenta una comparación entre ellas:

### Listas

- **Mutables:** Se pueden modificar después de su creación.
- **Ordenadas:** Mantienen el orden de inserción.
- **Permiten duplicados:** Pueden contener elementos repetidos.
- **Sintaxis:** Se definen con corchetes [].

```python
mi_lista = [1, 2, 3, 2, 4]
mi_lista.append(5)  # Añade un elemento
print(mi_lista)  # Output: [1, 2, 3, 2, 4, 5]
```

### Tuplas

- **Inmutables:** No se pueden modificar después de su creación.
- **Ordenadas:** Mantienen el orden de inserción.
- **Permiten duplicados:** Pueden contener elementos repetidos.
- **Sintaxis:** Se definen con paréntesis ().

```python
mi_tupla = (1, 2, 3, 2, 4)
# mi_tupla[0] = 5  # Esto causaría un error
print(mi_tupla)  # Output: (1, 2, 3, 2, 4)
```

### Sets

- **Mutables:** Se pueden modificar después de su creación.
- **No ordenados:** No mantienen un orden específico.
- **No permiten duplicados:** Cada elemento es único.
- **Sintaxis:** Se definen con llaves {} o la función set().

```python
mi_set = {1, 2, 3, 2, 4}
mi_set.add(5)  # Añade un elemento
print(mi_set)  # Output: {1, 2, 3, 4, 5}
```

Cada estructura tiene sus propios casos de uso. Las listas son versátiles y comúnmente usadas. Las tuplas son útiles para datos que no deben cambiar. Los sets son ideales para eliminar duplicados y realizar operaciones de conjuntos.

## Funciones en Python

Las funciones en Python son bloques de código reutilizables que realizan una tarea específica. Permiten organizar el código, mejorar la legibilidad y evitar la repetición.

### Definición de una función

En Python, se define una función usando la palabra clave 'def', seguida del nombre de la función y paréntesis que pueden contener parámetros:

```python
def saludar(nombre):
    return f"Hola, {nombre}!"

# Llamada a la función
mensaje = saludar("Ana")
print(mensaje)  # Output: Hola, Ana!
```

### Parámetros y argumentos

Los parámetros son variables listadas en la definición de la función. Los argumentos son los valores que se pasan a la función cuando se llama:

```python
def suma(a, b):
    return a + b

resultado = suma(3, 5)
print(resultado)  # Output: 8
```

### Argumentos por defecto

Python permite asignar valores por defecto a los parámetros:

```python
def potencia(base, exponente=2):
    return base ** exponente

print(potencia(3))     # Output: 9 (3^2)
print(potencia(3, 3))  # Output: 27 (3^3)
```

### *args y **kwargs

Python ofrece formas de pasar un número variable de argumentos a una función:

```python
# *args permite pasar un número variable de argumentos posicionales
def suma(*args):
    return sum(args)

print(suma(1, 2, 3, 4))  # Output: 10

# **kwargs permite pasar un número variable de argumentos con palabra clave
def info_persona(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")

info_persona(nombre="Juan", edad=30, ciudad="Madrid")
```

Las funciones son una parte fundamental de la programación en Python, permitiendo escribir código más modular y mantenible.

### Declaración return en funciones

La declaración 'return' se utiliza en funciones para especificar el valor que la función debe devolver cuando es llamada. Cuando se ejecuta una declaración 'return', la función termina inmediatamente y devuelve el valor especificado.

```python
def cuadrado(numero):
    return numero ** 2

resultado = cuadrado(4)
print(resultado)  # Output: 16
```

Puntos importantes sobre 'return':

- Una función puede tener múltiples declaraciones 'return', pero solo se ejecutará una.
- Si no se especifica un valor después de 'return', la función devolverá 'None'.
- Se puede devolver múltiples valores utilizando una tupla.

```python
def dividir_y_residuo(a, b):
    cociente = a // b
    residuo = a % b
    return cociente, residuo

resultado = dividir_y_residuo(17, 5)
print(resultado)  # Output: (3, 2)
```

El uso adecuado de 'return' es crucial para crear funciones efectivas y reutilizables en Python.

### Parámetros por defecto y múltiples returns

Los parámetros por defecto y múltiples returns son características avanzadas de las funciones en Python que proporcionan mayor flexibilidad en la programación.

```python
def calcular_precio(precio_base, descuento=0, impuesto=0.21):
    precio_con_descuento = precio_base * (1 - descuento)
    precio_final = precio_con_descuento * (1 + impuesto)
    
    return precio_con_descuento, precio_final

# Usando valores por defecto
precio_base, precio_final = calcular_precio(100)
print(f"Precio base: {precio_base}, Precio final: {precio_final}")

# Especificando descuento
precio_base, precio_final = calcular_precio(100, 0.1)
print(f"Precio con 10% descuento: {precio_base}, Precio final: {precio_final}")
```

Aspectos importantes a considerar:

- Los parámetros por defecto deben definirse al final de la lista de parámetros.
- Los valores por defecto se evalúan una sola vez cuando se define la función.
- Se pueden devolver múltiples valores separándolos por comas.
- Los valores devueltos se pueden asignar a variables individuales mediante desempaquetado.

## El Scope (Alcance) en Python

El scope o alcance en Python determina la visibilidad y accesibilidad de las variables en diferentes partes del código. Python tiene diferentes niveles de scope:

### Local Scope

Variables definidas dentro de una función que solo son accesibles dentro de esa función:

```python
def mi_funcion():
    x = 10  # variable local
    print(x)

mi_funcion()  # Output: 10
# print(x)  # Esto causaría un error porque x es local a mi_funcion()
```

### Global Scope

Variables definidas en el nivel principal del programa que son accesibles desde cualquier parte:

```python
y = 20  # variable global

def otra_funcion():
    print(y)  # Podemos acceder a la variable global
    
otra_funcion()  # Output: 20
```

### La palabra clave 'global'

Permite modificar una variable global desde dentro de una función:

```python
contador = 0

def incrementar():
    global contador
    contador += 1
    return contador

print(incrementar())  # Output: 1
print(contador)       # Output: 1
```

### Nonlocal Scope

Usado en funciones anidadas para acceder a variables de la función exterior:

```python
def funcion_exterior():
    x = 1
    def funcion_interior():
        nonlocal x
        x += 1
        return x
    return funcion_interior()

print(funcion_exterior())  # Output: 2
```

Entender el scope es crucial para escribir código Python efectivo y evitar errores comunes relacionados con la visibilidad de variables.