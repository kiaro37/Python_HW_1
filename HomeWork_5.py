# Задача 3.
# Sample Input
# ["eat", "tea", "tan", "ate", "nat", “bat"]
# Sample Output
# [ ["ate", "eat", "tea"], ["nat", "tan"], ["bat"] ]
# Т.е. сгруппировать слова по "общим буквам"

def group_words(words):
    result = []
    words_dict = {}
    for word in words:
        sorted_word = "".join(sorted(word))
        if not sorted_word in words_dict.keys():
            words_dict[sorted_word] = []
        words_dict[sorted_word].append(word)
    for key, value in words_dict.items():
        result.append(value)
    return result


input_list: list[str] = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(input_list)
print(group_words(input_list))

# Задача 6.
# Дана строка (возможно, пустая), состоящая из букв A-Z:AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB
# Нужно написать функцию RLE, которая на выходе даст строку вида: A4B3C2XYZD4E3F3A6B28 И сгенерирует ошибку,
# если на вход пришла невалидная строка. Пояснения: Если символ встречается 1 раз, он остается без изменений; Если
# символ повторяется более 1 раза, к нему добавляется количество повторений.

def rle_encode(letter):
    encoding = ''
    prev_char = ''
    count = 1
    if not letter:
        return ''
    for char in letter:
        if char != prev_char:
            if prev_char:
                encoding += prev_char + str(count)
            count = 1
            prev_char = char
        else:
            count += 1
    else:
        encoding += prev_char + str(count)
        return encoding


letter: str = "AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB"
print(letter)
print(rle_encode(letter))