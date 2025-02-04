n = int(input())
colors = input()

counter = 0
for i in range(1, n):
    if colors[i - 1] == colors[i]:
        counter += 1 

print(counter)

# RRGRRR