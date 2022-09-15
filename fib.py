
def fib(n):
    if n <= 2:
        return 1
    return fib(n-1) + fib(n-2)



def fib2(n, calculated = {}):
    if not n in calculated:
        if n <= 2:
            calculated[n] = 1
        else:
            calculated[n] = fib2(n-1,calculated) + fib2(n-2,calculated)
    return calculated[n]

print(fib2(500))
