import math

def palindrome(word):
    array = list(word)
    reformed = list(reversed(array))
    length = math.ceil(len(array) / 2)
    for i in range(length):
        if array[i] != reformed[i]:
            return False
    return True

print(palindrome('radar'))
print(palindrome('hello'))