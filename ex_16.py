# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

number = int(input("Введите число: "))
step = 2
form_list = []

while step <= number:
    if number % step == 0:
        form_list.append(step)
        number //= step
        step = 2
    else:
        step += 1

print(f"Простые множители числа  -> {form_list}")
