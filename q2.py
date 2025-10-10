odd_lst = {}
even_lst = {}


def number_info(n):

    if n < 0:
        print("Just Positive")
        return
    elif n > 0:
        if n % 2 != 0:
            odd = lambda n: n * 2
            odd_lst.update({n: odd(n)})
        else:
            even = lambda n: n**2
            even_lst.update({n: even(n)})
        n -= 1

        return number_info(n)

    odd_lst.update(even_lst)
    mykeys = list(odd_lst.keys())
    mykeys.sort()
    final_lst = {i: odd_lst[i] for i in mykeys}
    print(final_lst)

    only_values = list(map(lambda x: x, final_lst.values()))
    print(only_values)

number_info(5)
