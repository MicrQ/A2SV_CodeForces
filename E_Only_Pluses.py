n = int(input())

max_value = 0
for i in range(n):
    a, b, c = [int(num) for num in input().split()]

    #1: 3,3,4
    #2: 4,3,4
    #3: 4,4,4
    #4: 5,4,4
    #5: 5,5,4

    for i in range(5):
        if a <= b <= c or a <= c <= b:
            a += 1
        elif b <= a <= c or b <= c <= a:
            b += 1
        elif c <= a <= b or c <= b <= a:
            c += 1
        else:
            pass

    print(a * b * c)