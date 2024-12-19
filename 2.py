f1 = 1
f2 = 1
sum = 0

while(f1 < 4000000):
    if f1 % 2 == 0:
        sum += f1
    temp = f2
    f2 += f1
    f1 = temp

print(sum)