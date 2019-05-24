'''
Exercise 3: Write a program to read through a mail log, build a histogram using a dictionary to count how many messages have come from each email address, and print the dictionary.

Enter file name: mbox-short.txt
{'gopal.ramasammycook@gmail.com': 1, 'louis@media.berkeley.edu': 3,
'cwen@iupui.edu': 5, 'antranig@caret.cam.ac.uk': 1,
'rjlowe@iupui.edu': 2, 'gsilver@umich.edu': 3,
'david.horwitz@uct.ac.za': 4, 'wagnermr@iupui.edu': 1,
'zqian@umich.edu': 4, 'stephen.marquard@uct.ac.za': 2,
'ray@media.berkeley.edu': 1}
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


def main(argv):
    email_file = utils.open_file_to_handle(argv)
    sender_histogram = build_sender_histogram(email_file)
    print(sender_histogram)
    return


if __name__ == "__main__":
    main(sys.argv[1:])