friends = int(input())

presents = [int(i) for i in input().split()]

present_pairs = {}

for i, v in enumerate(presents, 1):
    present_pairs[v] = i

concatinated = ''
for i in range(1, len(present_pairs) + 1):
    concatinated += str(present_pairs[i]) + ' '

print(concatinated[:-1])
