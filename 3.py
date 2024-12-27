import math

def factors(num):
    upto = math.ceil(math.sqrt(num))
    list_of_factors = []
    
    for i in range(1, upto+1):
        if num % i == 0:
            list_of_factors.append(i)
            if i != num // i:
                list_of_factors.append(i)
            
    return sorted(list_of_factors, reverse=True)

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True



def largest_prime_factor(num):
    prime_factors = factors(num)
    for factor in prime_factors:
        if is_prime(factor):
            print(factor)
            break

largest_prime_factor(600851475143)