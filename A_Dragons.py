strength, dragons_num = [int(num) for num in input().split()]

dragons = []

for i in range(dragons_num):

    dragons.append(tuple(map(int, input().split())))

dragons.sort(key=lambda x: x[0])

for dragon, bonus in dragons:

    if dragon > strength:
        print('NO')
        break
    strength += bonus

else:
    print('YES')
