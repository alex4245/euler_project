def euler5(n):
    min_number = 2
    for i in range(2, n):
        old_min_number = min_number
        while True:
            if not min_number % i:
                while min_number % old_min_number:
                    min_number += i
                else:
                    break
            min_number += 1
    return min_number

print(euler5(20))

