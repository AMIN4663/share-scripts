def number_info(n):
    if n < 0:
        print("The number must be positive")
        return None
    def rec(i):
        if i == 0:
            return
        rec(i - 1)
        print(i, end =" ")
    rec(n)
number_info(-2)



    
