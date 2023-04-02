# Задача 3.
# Sample Input
# ["eat", "tea", "tan", "ate", "nat", “bat"]
# Sample Output
# [ ["ate", "eat", "tea"], ["nat", "tan"], ["bat"] ]
# Т.е. сгруппировать слова по "общим буквам"

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
