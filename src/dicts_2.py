'''
Exercise 2: Write a program that categorizes each mail message by which day of the week the commit was done. 
To do this look for lines that start with "From", then look for the third word and keep a running count of each of the days of the week. 
At the end of the program print out the contents of your dictionary (order does not matter).

Sample Line:
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

Sample Execution:
python dow.py
Enter a file name: mbox-short.txt
{'Fri': 20, 'Thu': 6, 'Sat': 1}
'''

import sys, utils

def is_proper_sender_line(word_list):
    return (len(word_list) > 2 and word_list[0] == "From")

def extract_weekday(word_list):
    return word_list[2]

def count_sending_weekdays_from_emails(email_file_handle):

    weekday_counts = dict()
    default_value_if_key_not_found = 0

    for line in email_file_handle:

        words = line.split()

        if is_proper_sender_line(words):
            weekday = extract_weekday(words)
            weekday_counts[weekday] = weekday_counts.get(weekday, default_value_if_key_not_found) + 1
    
    return weekday_counts

def print_weekday_counts(weekday_counts):
    print(weekday_counts)

def main(argv):

    email_file_to_read = utils.open_file_to_handle(argv)

    weekday_counts = count_sending_weekdays_from_emails(email_file_to_read)

    print_weekday_counts(weekday_counts)

    return

if __name__ == "__main__":
    main(sys.argv[1:])