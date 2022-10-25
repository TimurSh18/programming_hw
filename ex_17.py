# Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности.

numbers = list(map(int, input("Введите числа для списка: ").split()))
new_list = []
for i in numbers:
    if i not in new_list:
        new_list.append(i)
print(new_list)