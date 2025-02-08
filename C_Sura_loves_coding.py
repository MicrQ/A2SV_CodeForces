length = int(input())
string = input()

reverse_dac = []

for i in range(length - 1, -1, -1):
    mid = len(reverse_dac) // 2
    reverse_dac.insert(mid, string[i])

print(''.join(reverse_dac))