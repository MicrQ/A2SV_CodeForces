n = int(input())

""" taking a word and outputiing the abbrivated version
    of the word if it has more that 10 characters.

    n times.
"""

for i in range(n):
    
    word = input()
    word_length = len(word)

    # checking if the word has more that 10 characters
    if word_length <= 10:
        print(word)

    else:
        print(word[0] + str(word_length - 2) + word[-1])
