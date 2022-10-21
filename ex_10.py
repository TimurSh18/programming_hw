

def elements_sum(array=[], sum = 0,):
    if len(array) > 1:
        return sum + array[1] + elements_sum(array[2:], sum)
    else:
        return sum

numbers_list = list(
    map(int, input('Введите числа через пробел: ').split()))
print(f'Сумма чисел на нечетных позициях: {elements_sum(numbers_list)}')
        
