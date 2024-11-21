def suma_with_range(min, max):
  print(min, max)
  sum = 0
  for x in range(min, max):
    sum += x
  return sum

result = suma_with_range(1, 10)
print(result)
result_2 = suma_with_range(result, result + 10)
print(result_2)


result_3 = suma_with_range(result_2, result_2 + 10)
print(result_3)