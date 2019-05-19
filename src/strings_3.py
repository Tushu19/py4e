'''
Exercise 3: Encapsulate this code in a function named count, and generalize it so that it accepts the string and the letter as arguments.

word = 'banana'
count = 0
for letter in word:
    if letter == 'a':
        count = count + 1
print(count)

'''

def count_letter_a(word):
    return word.count('a')

def main():
    word = input('Please input word: ')
    print(count_letter_a(word))

main()