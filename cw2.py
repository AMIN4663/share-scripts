odd_lst = {}
even_lst = {}


def number_info(n):

    if n < 0:
        print("Just Positive")
        return
    elif n > 0:
        # print(n)
        if n % 2 != 0:
            odd = lambda n: n * 2
            odd_lst.update({n: odd(n)})
        else:
            even = lambda n: n**2
            even_lst.update({n: even(n)})
        n -= 1

        return number_info(n)

    # print(odd_lst)
    # print(even_lst)
    odd_lst.update(even_lst)
    # print(odd_lst)
    mykeys = list(odd_lst.keys())
    mykeys.sort()
    # print(mykeys)
    final_lst = {i: odd_lst[i] for i in mykeys}
    print(final_lst)


number_info(5)
