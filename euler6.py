from functools import reduce
sum = reduce(lambda a, b: a + b, [i for i in range(101)])
sq_sum = sum * sum
sum_sq = reduce(lambda a, b: a + b, [i * i for i in range(101)])
print(sq_sum - sum_sq)
