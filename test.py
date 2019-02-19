from itertools import permutations
test = []
for x in range(1,4):
    test.append(x)

print(list(permutations(test,3)))
