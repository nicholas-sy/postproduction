def fib(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(1, n):
        a, b = b, a + b
    return b

def fib_even_sum(max):
    total = 0
    for x in range(2, max):
        if fib(x) > max:
            return(total)
        if fib(x) % 2 == 0:
            total += fib(x)
        else:
            total = total

print(fib_even_sum(4000000000000000000000000000))
