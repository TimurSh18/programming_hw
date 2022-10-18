# Реализуйте алгоритм перемешивания списка
import random

n = 5

array = []
for i in range(n):
    a = random.randint(1, n+1)
    array.append(a)
print(array)
random.shuffle(array)
print(array)
