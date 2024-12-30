import math

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


count = 0
i = 1
while (True):
  if is_prime(i): count += 1
  if count == 10001: break
  i += 1

print(i)

  