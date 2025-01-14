def count_fruit(fruit_name):
    fruits = ['사과','배','배','감','수박','귤','딸기','사과','배','수박']
    count = 0

    for f in fruits:
        if f == fruit_name:
            count += 1

    return count

print(count_fruit('사과'))
print(count_fruit('배'))
print(count_fruit('감'))

