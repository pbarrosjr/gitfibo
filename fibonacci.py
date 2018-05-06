# fibonnaci start here


def fib(n):
    a, b = 1, 0
    for i in range(n):
        yield b
        a, b = b, a+b


for i in fib(10):
    print i
