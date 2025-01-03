def alphabetical_value(word):
  value = 0
  for character in word:
    value += ord(character) % 64
  
  return value


with open('./names.txt', 'r') as file:
  names = file.read().strip().split(",")

names = sorted([name[1:-1] for name in names])

sum = 0
for index, name in enumerate(names):
  sum += alphabetical_value(name) * (index + 1)

print(sum)