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


def triangle_num(upto):
    current = 1
    i = 1

    while True:
        i += 1
        current += i

        if len(factors(current)) >= upto:
            print(current)
            break


triangle_num(500)