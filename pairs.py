m = int(input())
n = int(input())


def generator_pairs(start, end):
    list_pairs = []
    for item in range(start, end + 1):
        for elem in range(item, end + 1):
            list_pairs.append((item, elem))
    return list_pairs


print(generator_pairs(m, n))
