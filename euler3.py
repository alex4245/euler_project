def factorization(n):
    prime_fact = []
    i = 2
    while i <= n:
        if not n % i:
            prime_fact.append(i)
            n = n / i
        else:
            i += 1
    return prime_fact

print (max(factorization(600851475143)))