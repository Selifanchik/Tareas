number = int(input())


def prev_mult_of_three(num):
    denominator = True
    length_num = len(str(num))
    while length_num > 0 and denominator:
        if int(str(num)[0:length_num]) % 3 == 0:
            denominator = False
            return int(str(num)[0:length_num])
        else:
            length_num -= 1
    if denominator:
        return 'null'


print(prev_mult_of_three(number))
