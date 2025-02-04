testcases = int(input())

""" taking input testcases times and checking
    for their indices difference with the string 'codeforces'
"""
codeforces = 'codeforces'

# iterating for each testcase
for testcase in range(testcases):

    # taking input and initializing different indices
    test_word = input()
    counter = 0

    for i in range(len(codeforces)):

        # checking if characters at same index differ
        if codeforces[i] != test_word[i]:
            counter += 1

    print(counter)
