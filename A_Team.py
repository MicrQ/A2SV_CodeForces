n = int(input())

""" taking input and checking
    if they are going to write the implementation
"""

implemented = 0
for i in range(n):
    status = [int(num) for num in input().split()]

    if status.count(1) >= 2:
        implemented += 1

print(implemented)