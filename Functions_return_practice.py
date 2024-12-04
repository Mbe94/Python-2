# Ejercicios Nivel 1
# Suma de dos números: Escribe una función suma que tome dos argumentos (números) y retorne su suma.

def suma(a,b):
    return a+b

resultado = suma(10,15)
print(resultado)

#---------------------------------------------------------------------------------------------------

# Área de un triángulo
# Crea una función area_triangulo que reciba la base y la altura de un triángulo y retorne su área.

def area_triangulo(base,altura):
    return ((base * altura)/2)

resultado_area = area_triangulo(5,10)
print(resultado_area)

#---------------------------------------------------------------------------------------------------

# Obtener el cuadrado de un número
# Escribe una función cuadrado que reciba un número y retorne su cuadrado.

def cuadrado(x):
    return (x * x)

resultado_cuadrado = cuadrado(4)
print(resultado_cuadrado)

#---------------------------------------------------------------------------------------------------

# Convertir grados Celsius a Fahrenheit
# Define una función celsius_a_fahrenheit que convierta una temperatura dada en grados Celsius a Fahrenheit y la retorne.

def celsius_a_fahrenheit(c):
    return ((9 % 5 )*c)+32

resultado_grados = celsius_a_fahrenheit(100)
print(resultado_grados)

#---------------------------------------------------------------------------------------------------

# Concatenar palabras
# Crea una función concatenar que tome dos cadenas de texto y retorne su concatenación.

def conc(x,y):
    return x+y

resultado_concatenacion = conc("Hola ","Mundo")
print(resultado_concatenacion)

#---------------------------------------------------------------------------------------------------
