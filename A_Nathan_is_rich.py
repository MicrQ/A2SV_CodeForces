testcases = int(input())

for i in range(testcases):

    wheels = int(input())

    if wheels % 4 == 0:
        print(wheels // 4)

    else:
        print(wheels // 4 + 1)
