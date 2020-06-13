max_palindrome = 0
for i in range(100, 999):
    for j in range(i, 999):
        mult = i * j
        mult_str = str(mult)
        if mult_str == mult_str[::-1] and int(mult) > max_palindrome:
            max_palindrome = mult

print (max_palindrome)

print(max([i * j for i in range(100, 999) for j in range(i, 999) if str(i*j) == str(i*j)[::-1]]))