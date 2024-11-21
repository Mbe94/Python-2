#Cuadrados de números

'Crea una lista que contenga los cuadrados de los números del 1 al 10'

cuadrados = [ i * i for i in range (1,11)]
print(cuadrados)

#----------------------------------------

#Números pares

"Genera una lista con todos los números pares del 1 al 20."

pares = [i for i in range(1,21) if i % 2 == 0]
print(pares)

#----------------------------------------

#Nombres en minúsculas

"Tienes una lista de nombres: ['Ana', 'Carlos', 'MARCOS', 'luisa']." 
"Usa una list comprehension para convertir todos los nombres a minúsculas."

nombre = ['Ana', 'Carlos', 'MARCOS', 'luisa']
nombres_minuscula = [nombre.lower() for nombre in nombre]
print(nombres_minuscula)

#----------------------------------------

#Filtrar palabras largas

"Dada una lista de palabras: ['casa', 'elefante', 'sol', 'biblioteca', 'auto']" 
"crea una nueva lista que solo contenga palabras con más de 4 letras."

palabra = ['casa', 'elefante', 'sol', 'biblioteca', 'auto']
palabras_cortas = [palabra for palabra in palabra if len(palabra) > 4]
print(palabras_cortas)


#----------------------------------------

#Multiplicación de números

"Crea una lista que contenga los resultados de multiplicar los números del 1 al 5 por 3" 

multiplicacion = [i * 3 for i in range(1,6)]
print(multiplicacion)

#----------------------------------------

#Lista de vocales

"Dada una cadena de texto: programación, crea una lista que contenga solo las vocales de la palabra." 

word = 'programación'
vocales = [i for i in word if i in 'aeiouáéíóú']
print(vocales)

#----------------------------------------

#Números divisibles por 3

"Genera una lista con todos los números del 1 al 50 que sean divisibles por 3." 

divisiblestres = [i for i in range(1,51) if i % 3 == 0]
print(divisiblestres)

#----------------------------------------

#Longitud de palabras

"Dada la lista: ['hola', 'python', 'ejercicio', 'list', 'comprehension']" 
"genera una nueva lista con la longitud de cada palabra." 

longpalabras = ['hola', 'python', 'ejercicio', 'list', 'comprehension']
long = [len(i) for i in longpalabras ]
print(long)

#----------------------------------------

#Valores positivos

"Dada una lista de números: [-10, 15, -20, 30, -5, 50]" 
"crea una lista que solo contenga los números positivos." 

valores = [-10, 15, -20, 30, -5, 50]
valpos = [i for i in valores if i > 0 ]
print(valpos)

#----------------------------------------

#Crear una tabla de multiplicar

"Crea una lista que contenga los resultados de la tabla de multiplicar del 5 (del 5 al 50)."  

valpos = [i * 5 for i in range(1,11) ]
print(valpos)


#----------------------------------------

#Duplicar los valores de una lista: Dada la lista numbers = [1, 2, 3, 4, 5], crea una nueva lista donde cada número sea multiplicado por 2.

numbers2 = [1,2,3,4,5]
newnumbers2 = [i * 2 for i in numbers2 ]
print(newnumbers2)

#----------------------------------------

#Filtrar números mayores que 5: Dada la lista numbers = [3, 4, 5, 6, 7, 8], crea una nueva lista que contenga solo los números mayores que 5.

numbers3 = [3,4,5,6,7,8]
newnumbers3 = [i for i in numbers3 if i > 5 ]
print(newnumbers3)

#----------------------------------------

#Obtener las primeras letras de los nombres: Dada la lista names = ["Ana", "Juan", "Pedro", "Maria"], crea una nueva lista con solo las primeras letras de los nombres.

names = ["Ana", "Juan", "Pedro", "Maria"]
primeras_letras = [nombre[0] for nombre in names]
print(primeras_letras)

#----------------------------------------

#Filtrar los números impares: Dada la lista numbers = [1, 2, 3, 4, 5, 6], crea una nueva lista que contenga solo los números impares.

numbers4 = [1, 2, 3, 4, 5, 6]
newnumbers4 = [i for i in numbers4 if i % 2 != 0]
print(newnumbers4)

#----------------------------------------

#Multiplicar por 3 y filtrar números menores que 10: Dada la lista numbers = [1, 3, 5, 7, 9], crea una nueva lista con los números multiplicados por 3 que sean menores que 10.

numbers5 = [1, 3, 5, 7, 9]
newnumbers5 = [i for i in numbers5 if i * 3 < 10  ]
print(newnumbers5)

#----------------------------------------

#Filtrar palabras que contienen una letra específica: Dada la lista words = ["banana", "manzana", "melon", "pera"], genera una nueva lista que contenga las palabras que contienen la letra "a".

words = ["banana", "manzana", "melon", "pera"]
palabras_con_a = [palabra for palabra in words if 'a' in palabra]
print(palabras_con_a)

#----------------------------------------

#Crear una lista con el cuadrado de los números divisibles por 3: Dada la lista numbers = [1, 2, 3, 4, 5, 6, 9, 12], crea una nueva lista que contenga el cuadrado de los números que son divisibles por 3.

numbers6 = [1, 2, 3, 4, 5, 6, 9, 12]
newnumbers6 = [i*i for i in numbers6 if i % 3 ==0]
print(newnumbers6)