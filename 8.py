upto = 13
largest = 0
num_str = ''
with open('./8.txt', 'r') as file:
    for line in file:
        num_str += line.strip()


for i in range(len(num_str) - upto + 1):
    product = 1
    for j in range(upto):
        product *= int(num_str[i+j])
    if product > largest:
        largest = product

print(largest)
