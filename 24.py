from itertools import permutations

perm = list(permutations(["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]))
n = 1000000

print("".join(perm[n-1]))