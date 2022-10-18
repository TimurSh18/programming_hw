# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

def multiplication(n):
    array = []
    digit = 1
    for i in range(1, n):
        array.append(digit)
        digit = digit*(i+1)
        print(array)

n = 5
multiplication(n)