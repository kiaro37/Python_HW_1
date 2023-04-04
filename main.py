# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному
# диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)

def index_array(int_arr: list):
    len_list = int(input("Введите количество жлементов: "))
    new_list = []
    for i in range(len_list):
        int_arr.append(int(input(f"Введите {i+1} элемент: ")))

    min_ind = int(input("Введите минимальный индекс: "))
    max_ind = int(input("Введите максимальный индекс: "))

    print(int_arr)

    for i in range(len_list):
        if i > min_ind and i < max_ind:
            new_list.append(i)

    print(new_list)



input_list: list = []
index_array(input_list)