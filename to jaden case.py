excerption = input()


def to_jaden_case(quote):
    quote_list = list(map(str, quote.split()))
    return ' '.join([x.capitalize() for x in quote_list])


print(to_jaden_case(excerption))
