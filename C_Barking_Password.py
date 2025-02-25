password = input()

words = int(input())

barks = [input() for i in range(words)]

string = ''.join(barks)

if password in string or password in string[::-1] or password in ''.join(barks[::-1]):
    print('YES')
else:
    print('NO')