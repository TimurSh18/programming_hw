# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов

def fibbonachi(numb):
    array = [1,0,1]
    for i in range(1, numb):
        array.insert(0, array[1] - array[0])
        array.append(array[-2] + array[-1])
    return array

num = int(input('Введите число: '))
print(fibbonachi(num))