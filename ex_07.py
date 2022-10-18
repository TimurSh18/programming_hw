# Задайте список из n чисел последовательности (1+ 1/n)^n и выведите на экран их сумму.

number = int(input("Введите число: "))
sum_main = 0

for i in range(1, number + 1 ):
    rounding = round((1+1/i)**i, 1)
    sum_main += rounding
    print(rounding)
print(f'Сумма чисел = {sum_main}')