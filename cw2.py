def number_info(n):
    if n < 0:
        print("not Positive")
        return
    elif n > 0:
        print(n)
        n = n - 1
        number_info(n)
