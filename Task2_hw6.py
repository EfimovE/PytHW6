# Задайте список из n чисел последовательности 
# (1+1/n)^n и выведите на экран их сумму.

# def sequence (N):
#     array = []
#     n = 1
#     sum = 0
#     for i in range (1, N + 1):
#         num = (1+1/n)**n
#         sum += num
#         array.append(num)
#         n += 1
#     print (f'Сумма элементов последовательности = {sum}')
#     return array

# num = int (input ('Введите натуральное число: '))
# array = sequence (num)
# print (array)

n = int(input("Введите количество вводимых чисел:  "))

list = [(1+1/i)**i for i in range(1, n + 1)] 
print(list)
print(round(sum(list), 2))