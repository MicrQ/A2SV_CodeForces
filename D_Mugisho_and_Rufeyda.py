digits, divisor = (map(int, input().split()))

max_num = 10 ** digits
min_num = 10 ** (digits - 1)

while min_num < max_num:
    val = min_num // divisor
    if min_num % divisor == 0:
        print(min_num)
        break

    else:
        min_num += 1

else:
    print(-1)