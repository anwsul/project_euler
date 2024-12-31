nums = []
with open('./13.txt', 'r') as file:
    for line in file:
        nums.append(int(line.strip()))

print(str(sum(nums))[:10])
