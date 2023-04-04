# Задача 30:  Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
#
def arithmetic(array: list):
    array.append(int(input("Введите первый элемент прогрессии: ")))
    dif = int(input("Введите разность элементов прогрессии: "))
    quantity = int(input("Введите количество элементов прогрессии: "))
    first_el = array[0]
    for i in range(2, quantity+1):
        array.append(first_el + (i - 1) * dif)

    return array


int_arr = []
print(arithmetic(int_arr))


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