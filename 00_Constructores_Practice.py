#Ejercicio 1: Crear una lista de cuadrados

#Usa range() para generar una lista de números del 1 al 10 y luego crea una lista que contenga sus cuadrados.

listacuadrados = [i*i for i in range(1,11)]
print(listacuadrados)

#--------------------------------------------------------

#Ejercicio 2: Crear un diccionario a partir de dos listas

#Usa zip() para combinar dos listas: una con los nombres de estudiantes y otra con sus calificaciones. Genera un diccionario que asigne a cada estudiante su calificación.

Lista_de_nombres = ["Ana", "Juan", "Pedro"]
Lista_de_calificaciones = [85, 90, 78]
notas = {k:v for k,v in zip(Lista_de_nombres,Lista_de_calificaciones)}
print(notas)

#--------------------------------------------------------

#Ejercicio 3: Agregar índices a una lista

#Usa enumerate() para crear un diccionario donde las claves sean los índices de una lista de frutas y los valores sean los nombres de las frutas.

frutas = ["manzana", "pera", "uva"]
listafrutas = {i: fruta for i, fruta in enumerate(frutas)}
print(listafrutas)

#--------------------------------------------------------

#Ejercicio 4: Filtrar y elevar al cuadrado los valores de un diccionario

#Usa dict.items() para iterar sobre un diccionario de números y sus valores. Crea un nuevo diccionario que solo incluya números pares y eleva sus valores al cuadrado.

Diccionario_original = {"a": 2, "b": 3, "c": 4}
dobledic = {a:b*2 for a,b in Diccionario_original.items()}
print(dobledic)

#--------------------------------------------------------

#Ejercicio 5: Ordenar palabras por longitud

#Usa sorted() para ordenar una lista de palabras en función de su longitud, de menor a mayor.

words = ["Python", "es", "genial"]
sorted_words = [word for word in sorted(words, key=len)]
print(sorted_words)

#--------------------------------------------------------

#Ingles
#Built-in Functios

#Task: Use range() to generate a list of even numbers from 2 to 20

even_numbers = [i for i in range(2, 21) if i % 2 == 0]
print(even_numbers)

#----------------------------

#Range
#Use range() to generate a list of numbers from 10 to 1 in descending order and print the list.

list_of_numbers = [ i for i in range(1,11)]
print(list_of_numbers)

#----------------------------

#Range
#Use range() to generate a list of multiples of 5 from 5 to 50 and print the list

list_of_multiples = [i for i in range(5,51,5)]
print(list_of_multiples)


#Task:
#Use range() to generate a list of odd numbers from 1 to 19 and print the list.

odd_numbers = [i for i in range(1, 20, 2)]
print(odd_numbers)

#Task:
#Write a Python program that prints all even numbers between 1 and 50, but instead of printing numbers divisible by 10, it should print "Skipped!".

for num in range(1, 51):  # Iterate from 1 to 50
    if num % 2 == 0:  # Check if the number is even
        if num % 10 == 0:  # Check if the number is divisible by 10
            print("Skipped!")
        else:
            print(num)
