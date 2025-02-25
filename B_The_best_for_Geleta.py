tests = int(input())

for test in range(tests):

    length, ops = [int(num) for num in input().split()]

    arr = [int(n) for n in input().split()]
    arr_max = arr.index(max(arr))

    for op in range(ops):

        opps = input().split()
        max_idx = arr_max

        for i in range(length):
            l, r = int(opps[1]), int(opps[2])

            if l <= arr[i] <= r:
                if opps[0] == '+':
                    arr[i] += 1
                else:
                    arr[i] -= 1

                max_idx = i if arr[max_idx] < arr[i] else max_idx

        print(f'{arr[max_idx]} ', end='')
    print()
