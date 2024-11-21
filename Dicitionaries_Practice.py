#--------------------------------------------

#Crea un diccionario donde las claves sean los números del 1 al 5 y los valores sean el cuadrado de cada número.

dict_square = {i: i**2 for i in range(1, 6)}
print(dict_square)

#--------------------------------------------

#Dado el siguiente listado de frutas, crea un diccionario donde las claves sean las frutas y los valores sean la longitud de cada nombre.

fruits = ['apple', 'banana', 'cherry', 'date']
dict_fruits = {fruit: len(fruit) for fruit in fruits}
print(dict_fruits)
