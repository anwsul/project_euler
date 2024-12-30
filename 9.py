import math

GOAL = 1000 ** 2 # equating the two equations gives us 1000^2 = 2000(a+b) - 2ab
done = False

for a in range(1, 500):
    if done: break
    for b in range(1, 500):
        goal = 2000 * (a + b) - 2 * a * b
        if goal == GOAL:
            print(a * b * (1000 - a - b)) #abc
            done = True
