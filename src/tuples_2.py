'''
Exercise 2: This program counts the distribution of the hour of the day for each of the messages. 
You can pull the hour from the "From" line by finding the time string and then splitting that string into parts using the colon character. 
Once you have accumulated the counts for each hour, print out the counts, one per line, sorted by hour as shown below.

python timeofday.py
Enter a file name: mbox-short.txt
04 3
06 1
07 1
09 2
10 3
11 6
14 1
15 2
16 4
17 2
18 1
19 1
'''

import sys, utils

def extract_timeofday_from_sender(email_line):
    words = email_line.split()
    timestamp = words[5]
    hour, minute, second = timestamp.split(':')
    return hour

def main(arguments):
    email_file_handle = utils.open_file_to_handle(arguments)
    timeofday_histogram = utils.process_sender_lines_to_dict(email_file_handle, extract_timeofday_from_sender)
    sorted_by_key = utils.sort_dict_by_keys(timeofday_histogram)
    utils.print_dict_by_line(sorted_by_key)
    return

if __name__ == "__main__":
    main(sys.argv[1:])