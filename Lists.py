#numbers = []
#for element in range(1, 11):
#  numbers.append(element* 2)
#print(numbers )

#numbers_V2 = [element *2 for element in range(1, 11)]
#print(numbers_V2)

numbers = []
for i in range(1, 11):
    if i % 2 == 0:
        numbers.append(i*2)
print(numbers)

numbers_V2 = [i *2 for i in range(1, 11) if i % 2 == 0]
print(numbers_V2)