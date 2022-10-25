# Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100)
#  многочлена и записать в файл многочлен степени k.
from random import randint

k = randint(1,6)# степень

form_list =[]
for i in range (1, k+1):
    form_list.append(randint(0, 100))

while k>0:
    if k>=1:
        print(f"{randint(0,100)}x^{k}", end="+" '1')
    k -= 1