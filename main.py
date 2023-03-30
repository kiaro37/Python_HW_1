# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
#
# *Пример:*
#
# 5
#     1 2 3 4 5
#     6
#     -> 5

input_list = []
list_len = int(input("Введите количество элементов в массиве: "))
for _ in range(list_len-1):
    input_list.append(int(input("Введите число: ")))
for _ in range(1):
    input_list.append(int(input("Введите число X: ")))
print(input_list)
x: int = input_list[list_len-1]

input_list = set(input_list)
print(input_list)
input_list = list(input_list)
print(input_list)
y: int
for i in range(len(input_list)):
    if x == input_list[i]:
        y = input_list[i-1]
print(y)


