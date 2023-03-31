# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.
#

input_list_1 = []
list_1_len = int(input("Введите количество элементов в массиве 1: "))
for _ in range(list_1_len):
    input_list_1.append(int(input("Введите число: ")))

input_list_2 = []
list_2_len = int(input("Введите количество элементов в массиве 2: "))
for _ in range(list_2_len):
    input_list_2.append(int(input("Введите число: ")))

input_list_3 = []

input_list_1.sort()
input_list_2.sort()
print(input_list_1)
print(input_list_2)
for i in range(list_1_len):
    for j in range(list_2_len):
        if input_list_1[i] == input_list_2[j]:
            input_list_3.append(input_list_1[i])
input_list_3.sort()
input_list_3 = set(input_list_3)
print(input_list_3)



