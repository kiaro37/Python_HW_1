# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X.
# Попробуйте использовать метод count(), а также решите задачу с помощью своего алгоритма (без count).
# Замерьте время работы двух алгоритмов и сравните, подумайте, почему оно отличается.
#
# *Пример:*
#
# 5
#     1 2 3 4 5
#     3
#     -> 1

input_list = []
list_len = int(input("Введите количество элементов в массиве: "))
for _ in range(list_len-1):
    input_list.append(int(input("Введите число: ")))
for _ in range(1):
    input_list.append(int(input("Введите число X: ")))
print(input_list)
x: int = input_list[list_len-1]

import time
start = time.time()
totalizer: int = 0
for i in range(list_len):
    if input_list[i] == x:
        totalizer += 1
print(totalizer)
end = time.time()
print("The time of execution of above program is :", (end-start) * 10**3, "ms")

import time
start = time.time()
count = input_list.count(x)
print(count)
end = time.time()
print("The time of execution of above program is :", (end-start) * 10**3, "ms")

