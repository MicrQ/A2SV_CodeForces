n = int(input())

cards = [int(num) for num in input().split()]

tuple_cards = [(cards[i], i)for i in range(n)]
tuple_cards.sort()

right = n - 1
for left in range(n // 2):
    print(tuple_cards[left][1] + 1, tuple_cards[right][1] + 1)

    right -= 1

# [1,3,4,4,5,7] = 8

# [(1,0), (5,1), (7,2), (4,3), (4, 4), (3,5)]

# [(1,0), (3,5), (4,3), (4,4), (5, 1), (7,2)]