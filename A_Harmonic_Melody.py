melodies = int(input())

for i in range(melodies):
    notes = int(input())
    notes_of_m = [int(num) for num in input().split()]

    for i in range(notes - 1):
        interval = abs(notes_of_m[i + 1] - notes_of_m[i])

        if interval not in (5, 7):
            print('NO')
            break

    else:
        print('YES')