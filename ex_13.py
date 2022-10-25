# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

number = int(input("Введите число: "))

S = "Number = "
while number > 1:
    ost = number % 2
    number = number // 2
    count = str(ost)
    S += count
    print(number)

number = str(number)
S += number
print(S)