import math

def factors(num):
    upto = math.ceil(math.sqrt(num))
    list_of_factors = []
    
    for i in range(1, upto + 1):
        if num % i == 0:
            if i not in list_of_factors:
                list_of_factors.append(i)
            if i != num // i and num // i not in list_of_factors:
                list_of_factors.append(num // i)
            
    return sorted(list_of_factors)


def sum_of_factors(num):
    return sum(factors(num)[:-1])


def is_amicable(num):
    a = sum_of_factors(num)
    b = sum_of_factors(a)

    if b == num and a != b:
        return True
    return False

_sum = 0
for i in range(1, 10000):
    if is_amicable(i):
        _sum += i


print(_sum)