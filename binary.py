n = int(input())

def binary(n):
    item = n
    string_item = ''
    while item > 0:
        string_item = str(item % 2) + string_item
        item //= 2
    return string_item


print(binary(n))
print(160 | 148 | 128)

