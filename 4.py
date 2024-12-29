def reverse_num(num):
  reversed_num = 0

  while num != 0:
      digit = num % 10
      reversed_num = reversed_num * 10 + digit
      num //= 10

  return reversed_num


largest = 0
for i in range (100, 1000):
  for j in range(100, 1000):
    product = i * j
    if product == reverse_num(product) and product > largest:
       largest = product


print(largest)
