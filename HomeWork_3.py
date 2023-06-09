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
# print(input_list)
input_list = list(input_list)
input_list.sort()
print(input_list)
y: int
for i in range(len(input_list)):
    if x == input_list[i] and x != input_list[len(input_list)-1]:
        if x - input_list[i-1] > input_list[i+1] - x:
            y = input_list[i + 1]
        elif x - input_list[i-1] < input_list[i+1] - x:
            y = input_list[i - 1]
    if x == input_list[0]:
        y = input_list[1]
    if x == input_list[len(input_list)-1]:
        y = input_list[i-1]
print(y)


# *Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так:A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка; B, C, M, P – 3 очка; F, H, V, W, Y – 4 очка; K – 5 очков; J, X – 8 очков; Q, Z – 10 очков.
# А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко; Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка; Й, Ы – 4 очка; Ж, З, Х, Ц, Ч – 5 очков; Ш, Э, Ю – 8 очков; Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово,
# которое содержит либо только английские, либо только русские буквы.
#
# *Пример:*
#
# ноутбук
#     12

a_dict = {1: 'авеинорстaeioulnstr', 2: 'дклмпуdg', 3: 'бгёьяbcmp', 4: 'йыfhvwy', 5: 'жзхцчk', 8: 'шэюx', 10: 'фщъqz'}
text = input("Введите слово: ")
result = [key for words in text for key, value in a_dict.items() if words in value]
print(result)
print(sum(result))