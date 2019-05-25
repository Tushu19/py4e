'''
Exercise 1: Revise a previous program as follows: 
Read and parse the "From" lines and pull out the addresses from the line. 
Count the number of messages from each person using a dictionary.

After all the data has been read, print the person with the most commits by creating a list of (count, email) tuples from the dictionary. 
Then sort the list in reverse order and print out the person who has the most commits.

Sample Line:
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

Enter a file name: mbox-short.txt
cwen@iupui.edu 5

Enter a file name: mbox.txt
zqian@umich.edu 195
'''

import sys, utils


def extract_sender(email_sender_line):
    line_word_list = email_sender_line.split()
    return line_word_list[1]


def build_sender_histogram(email_file):
    sender_histogram = dict()

    for line in email_file:
        if utils.is_proper_sender_line(line):
            email_sender = extract_sender(line)
            sender_histogram[email_sender] = sender_histogram.get(email_sender, 0) + 1
    
    return sender_histogram


def get_biggest_sender(sender_histogram_dict):
    sorted_senders = sorted([(send_amount, sender) for sender, send_amount in sender_histogram_dict.items()], reverse = True)
    biggest_send_amount, biggest_sender = sorted_senders[0]
    return (biggest_sender, biggest_send_amount)


def main(argv):
    email_file = utils.open_file_to_handle(argv)
    sender_histogram = build_sender_histogram(email_file)
    biggest_sender, biggest_send_amount = get_biggest_sender(sender_histogram)
    print(biggest_sender, biggest_send_amount)
    return


if __name__ == "__main__":
    main(sys.argv[1:])