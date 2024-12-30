sum = 0
square_sum = 0

for i in range(1, 101):
  sum += i
  square_sum += i*i

sum_squared = sum * sum
print(sum_squared - square_sum)