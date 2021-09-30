number = int(input())


def sumin(n):
    sum_min = 0
    for item in range(1, n + 1):
        sum_min += (2 * n - (2 * item - 1)) * item
    return sum_min


def sumax(n):
    sum_max = 0
    for item in range(1, n + 1):
        sum_max += (2 * n - (2 * item - 1)) * (n - item + 1)
    return sum_max


def sumsum(n):
    return sumin(n) + sumax(n)


print(sumin(number))
print(sumax(number))
print(sumsum(number))
