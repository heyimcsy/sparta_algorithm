def findtext(s):
    char_index = {}
    start = 0
    length = 0

    for i, char in enumerate(s):
        if char in char_index and char_index[char] >= start:
            start = char_index[char] + 1

        char_index[char] = i
        length = max(length, i - start + 1)
    return length

print(findtext('abcabcbb'))
print(findtext('bbbbb'))