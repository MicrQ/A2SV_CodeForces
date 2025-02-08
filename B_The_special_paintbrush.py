testcases = int(input())

for i in range(testcases):

    length = int(input())
    string = input()

    left, right = 0, length - 1

    while left <= right:

        if string[left] == 'W':
            left += 1
        elif string[right] == 'W':
            right -= 1
        else:
            break

    print(right - left + 1)
