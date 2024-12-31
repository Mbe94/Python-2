#--------------------------------------------

#Crea un diccionario donde las claves sean los números del 1 al 5 y los valores sean el cuadrado de cada número.

dict_square = {i: i**2 for i in range(1, 6)}
print(dict_square)

#--------------------------------------------

#Dado el siguiente listado de frutas, crea un diccionario donde las claves sean las frutas y los valores sean la longitud de cada nombre.

fruits = ['apple', 'banana', 'cherry', 'date']
dict_fruits = {fruit: len(fruit) for fruit in fruits}
print(dict_fruits)

#--------------------------------------------

#Crea un diccionario donde las claves sean números del 1 al 10 y los valores sean los cuadrados de esos números.

dict_numbers = {i: i*i for i in range(1,11)}
print(dict_numbers)

#--------------------------------------------

#Crea un diccionario a partir de una lista de palabras, donde las claves sean las palabras y los valores su longitud.

palabras2 = ('Pais','Departamento','Provincia','Canton','Municipio')
dict_palabras2 = {word: len(word) for word in palabras2}
print(dict_palabras2)

#--------------------------------------------

#Genera un diccionario donde las claves sean letras de una palabra y los valores el número de veces que aparecen en esa palabra.

palabra3= "abracadabra"
dict_palabra3 = {word2: palabra3.count(word2) for word2 in palabra3}
print(dict_palabra3)

#--------------------------------------------

#Convierte dos listas en un diccionario donde una lista sea las claves y la otra los valores.

lista1= ('Bolivia','Chile','Argentina')
lista2= ('200','300','400')
lista3 = {claves : valores for (claves,valores) in zip(lista1,lista2)}
print(lista3)

#--------------------------------------------

#Genera un diccionario con las claves de 0 a 5 y como valores una lista con sus múltiplos hasta 10.

multiples_dict = {n: [n * i for i in range(1, 11)] for n in range(0, 6)}
print(multiples_dict)

#--------------------------------------------

#Dado un diccionario, genera uno nuevo con los mismos valores pero cuyas claves estén en mayúsculas.

original_dict = {"nombre": "Juan", "edad": 30, "pais": "Perú"}
uppercase_dict = {key.upper(): value for key, value in original_dict.items()}
print(uppercase_dict)

#--------------------------------------------

#Crea un diccionario que relacione cada número del 1 al 5 con su representación en palabras.

original_dict = {"nombre": "Juan", "edad": 30, "pais": "Perú"}
uppercase_dict = {key.upper(): value for key, value in original_dict.items()}
print(uppercase_dict)