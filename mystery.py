import math
number = int(input())


def route_cut(fl, start_cut, end_cut):
    if fl == 'start':
        start_cut += ((end_cut - start_cut) // 2)
    else:
        end_cut -= ((end_cut - start_cut) // 2)
    return start_cut, end_cut


def function_t(n):
    res = ['0', '1']
    if n > 1:
        for i in range(1, n):
            res_null = [('0' + x) for x in res]
            res_one = [('1' + x) for x in list(reversed(res))]
            res = res_null + res_one
    return res


def binary(n):
    item = n
    string_item = ''
    while item > 0:
        string_item = str(item % 2) + string_item
        item //= 2
    return string_item


def mystery(n):
    if n > 0:
        route = {'start': 'end', 'end': 'start'}
        a = math.log2(n + 1)
        binary_num = ''
        start_n = 0
        end_n = 2**math.ceil(a)
        flagg = 'end'
        while end_n - start_n > 1:
            if n >= (start_n + ((end_n - start_n) // 2)) and flagg == 'end':
                flagg = route[flagg]
                binary_num += '1'
            elif n < (end_n - ((end_n - start_n) // 2)) and flagg == 'start':
                flagg = route[flagg]
                binary_num += '1'
            else:
                binary_num += '0'
            start_n, end_n = route_cut(flagg, start_n, end_n)
        return int(binary_num, 2)
    else:
        return 0


def mystery_inv(n):
    if n > 0:
        route = {'start': 'end', 'end': 'start'}
        start_n = 0
        end_n = 2**(len(binary(n))) - 1
        flagg = 'end'
        for elem in binary(n):
            if elem == '1':
                flagg = route[flagg]
            start_n, end_n = route_cut(flagg, start_n, end_n)
        return end_n
    else:
        return 0


def name_of_mystery():
    pass


#print(binary(number))
print(mystery(number))
#print(function_t(number))
#print(mystery_inv(number))