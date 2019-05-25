'''
Exercise 5: This program records the domain name (instead of the address) 
where the message was sent from instead of who the mail came from (i.e., the whole email address). 
At the end of the program, print out the contents of your dictionary.

python schoolcount.py
Enter a file name: mbox-short.txt
{'media.berkeley.edu': 4, 'uct.ac.za': 6, 'umich.edu': 7,
'gmail.com': 1, 'caret.cam.ac.uk': 1, 'iupui.edu': 8}
'''

import sys, utils

def extract_domain(email_sender_line):
    words = email_sender_line.split()
    sender_email = words[1]
    email_domain = sender_email.split('@')[1]
    return email_domain


def count_email_domains(email_file_handle):
    email_domain_histogram = dict()

    for line in email_file_handle:
        if utils.is_proper_sender_line(line):
            domain = extract_domain(line)
            email_domain_histogram[domain] = email_domain_histogram.get(domain, 0) + 1

    return email_domain_histogram


def main(argument_list):
    email_file_handle = utils.open_file_to_handle(argument_list)
    email_domain_histogram = count_email_domains(email_file_handle)
    print(email_domain_histogram)
    return


if __name__ == "__main__":
    main(sys.argv[1:])