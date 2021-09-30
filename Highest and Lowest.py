string_number = input()


def high_and_low(numbers):
    max_number = max(list(map(int, numbers.split())))
    min_number = min(list(map(int, numbers.split())))
    return f'{max_number} {min_number}'


print(high_and_low(string_number))
