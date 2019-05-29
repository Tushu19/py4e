'''
Exercise 1: Write a simple program to simulate the operation of the grep command on Unix. 
Ask the user to enter a regular expression and count the number of lines that matched the regular expression:

$ python grep.py
Enter a regular expression: ^Author
mbox.txt had 1798 lines that matched ^Author

$ python grep.py
Enter a regular expression: ^X-
mbox.txt had 14368 lines that matched ^X-

$ python grep.py
Enter a regular expression: java$
mbox.txt had 4175 lines that matched java$
'''

import sys, re, utils


def count_regex_in_file(input_file_handle, regex_to_count):
    matching_line_count = 0
    for line in input_file_handle:
        line = line.rstrip()
        if re.search(regex_to_count, line):
            matching_line_count += 1

    return matching_line_count


def get_input_regex():
    input_regex = input('Enter a regular expression: ')
    return input_regex


def main(arguments):
    file_handle = utils.open_file_to_handle(arguments)
    input_regex = get_input_regex()
    regex_line_count = count_regex_in_file(file_handle, input_regex)
    print('The file had', regex_line_count, 'lines that matched', input_regex)
    return


if __name__ == "__main__":
    main(sys.argv[1:])