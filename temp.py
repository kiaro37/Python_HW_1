s = int(input('Введите число: '))
if s % 6 == 0:
    k = int(s/3*2)
    p = int((s - k)/2)
    print(f'{s} -> {p}, {k}, {p}')
else:
    print(f'Со значением {s} данная задача не может быть решена в целых числах.')