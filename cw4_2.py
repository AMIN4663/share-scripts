def number_info(n):
    if n < 0:
        print("The number must be positive")
        return None
    def rec(i):
        if i == 0:
            return
        rec(i - 1)
        sqr=(lambda i:i**2)
        dbl=(lambda i:i*2)
        if i%2==0:
            print(f"zog:{sqr(i)}")
        else:
            print(f'fard:{dbl(i)}')
    rec(n)
number_info(7)




    
