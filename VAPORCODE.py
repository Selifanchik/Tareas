string_input = input()


def vaporcode(s):
    return '  '.join(list(s.upper().replace(' ', '')))


vaporcode(string_input)
