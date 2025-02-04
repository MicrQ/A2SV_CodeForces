n = int(input())

for i in range(n):

    testcase = int(input())

    if testcase <= 1399:
        print('Division 4')
    elif testcase <= 1599:
        print('Division 3')
    elif testcase <= 1899:
        print('Division 2')
    else:
        print('Division 1')
