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
