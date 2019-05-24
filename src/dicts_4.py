'''
Exercise 4: Add code to the above program (dicts_3.py) to figure out who has the most messages in the file. 
After all the data has been read and the dictionary has been created, 
look through the dictionary using a maximum loop (see Chapter 5: Maximum and minimum loops) 
to find who has the most messages and print how many messages the person has.

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
    biggest_send_amount = 0
    biggest_sender = None
    
    for sender in sender_histogram_dict:
        send_amount = sender_histogram_dict[sender] 

        if send_amount > biggest_send_amount:
            biggest_send_amount = send_amount
            biggest_sender = sender
    
    return (biggest_sender, biggest_send_amount)


def main(argv):
    email_file = utils.open_file_to_handle(argv)
    sender_histogram = build_sender_histogram(email_file)
    biggest_sender, biggest_send_amount = get_biggest_sender(sender_histogram)
    print(biggest_sender, biggest_send_amount)
    return


if __name__ == "__main__":
    main(sys.argv[1:])