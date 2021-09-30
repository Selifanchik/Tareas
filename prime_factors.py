number = int(input())


def prime_factors(num):
    string_part = str()
    count = 0
    denominator = 2
    while num > 1:
        while num % denominator == 0:
            count += 1
            num //= denominator
        if count == 1:
            string_part += f'({denominator})'
        elif count > 0:
            string_part += f'({denominator}**{count})'
        denominator += 1
        count = 0
    return string_part


print(prime_factors(number))

