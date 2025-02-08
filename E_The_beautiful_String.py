testcases = int(input())

check = '1100'

for test in range(testcases):
    bits = input()
    bits_list = list(bits)
    queries = int(input())

    for query in range(queries):
        i, bit = (map(int, input().split()))

        bits_list[i - 1] = str(bit)
        bits = ''.join(bits_list)
        # print(bits)

        if check in bits:
            print('YES')
        else:
            print('NO')