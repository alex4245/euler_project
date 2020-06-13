def fib():
    a, b = 0, 1
    while True:
        a, b = b, a + b
        yield b

def euler2():
    result = 0
    for value in fib():
        if value > 4e6:
            break
        if not value % 2:
            result += value
    return result

print (euler2())


