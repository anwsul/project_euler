def collatz_count(start: int) -> int:
    current = start
    count = 0
    while (current != 1):
        if current % 2 == 0:
            current /= 2
        else:
            current = 3*current + 1
        count += 1

    return count


largest_count = 0
starting_num = 0
for i in range(1, 1000000):
    count = collatz_count(i)
    if count > largest_count:
        largest_count = count
        starting_num = i


print(starting_num)
