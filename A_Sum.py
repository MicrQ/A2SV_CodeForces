testcases = int(input())

for i in range(testcases):

    # taking a test case
    a, b, c = [int(num) for num in input().split()]

    if a + b == c or a + c == b or c + b == a:
        print('YES')
    else:
        print('NO')
