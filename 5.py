min_addition = 3 * 5 * 7 * 11 * 13 * 17 * 19
num = min_addition
while (True):
  found = True
  for i in range(11, 21):
    if num  % i != 0:
      found = False
      break
  
  if found:
    break
  num += min_addition


print(num)