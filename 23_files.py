file = open(r'C:\Users\Usuario\OneDrive\Escritorio\Python 2\text.txt')
#print(file.read())
#print(file.readline())
#print('prueba')

for line in file:
    print(line)
file.close()

with open('./text.txt') as file:
    for line in file:
        print(line)