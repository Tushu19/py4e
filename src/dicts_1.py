'''
Exercise 1: Download a copy of the file www.py4e.com/code3/words.txt

Write a program that reads the words in words.txt and stores them as keys in a dictionary. 
It doesn't matter what the values are. 
Then you can use the in operator as a fast way to check whether a string is in the dictionary.
'''

import sys
import utils

def count_words_from_file(file_handle_to_read):

    word_counts = dict()

    for line in file_handle_to_read:

        words = line.split()

        for word in words:

            word_counts[word] = word_counts.get(word, 0) + 1
    
    return word_counts


def main(argv):

    file_handle_to_read = utils.open_file_to_handle(argv)

    word_counts = count_words_from_file(file_handle_to_read)

    print(word_counts)

    return


if __name__ == "__main__":
    main(sys.argv[1:])