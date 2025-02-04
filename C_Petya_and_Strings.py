string1, string2 = [input().lower() for i in range(2)]

if string1 == string2:
    print(0)
elif string1 > string2:
    print(1)
else:
    print(-1)
