number = 10001
size = number
c, n = 1, 3

def refresh_parametrs(size):
    numbers = {i: None for i in range(3, size) if i % 2}
    numbers.update({2: True})
    return numbers

numbers = refresh_parametrs(size)
while c < number:
    if n >= size:
        size = 2 * size
        numbers = refresh_parametrs(size)
        c, n = 1, 3
    if numbers[n] is None:
        c += 1
        if c == number:
            break
        numbers[n] = True
        for i in range(n * n, size + 1, n):
            numbers[i] = False
    n += 2

print(n)








