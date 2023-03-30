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
print(input_list)
y: int
for i in range(len(input_list)):
    if x == input_list[i]:
        if x - input_list[i-1] > input_list[i+1] - x:
            y = input_list[i + 1]
        elif x - input_list[i-1] < input_list[i+1] - x:
            y = input_list[i - 1]
    elif x == input_list[0]:
        y = input_list[1]
    elif x == input_list[len(input_list)-1]:
        y = input_list[i-1]
print(y)