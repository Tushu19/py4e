'''
Exercise 5: Write a program to read through the mail box data. 
When you find line that starts with "From", you will split the line into words using the split function. 
We are interested in who sent the message, which is the second word on the From line.

From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008

You will parse the From line and print out the second word for each From line. 
Then you will also count the number of From (not From:) lines and print out a count at the end. 

This is a good sample output with a few lines removed:

python fromcount.py
Enter a file name: mbox-short.txt
stephen.marquard@uct.ac.za
louis@media.berkeley.edu
zqian@umich.edu

[...some output removed...]

ray@media.berkeley.edu
cwen@iupui.edu
cwen@iupui.edu
cwen@iupui.edu
There were 27 lines in the file with From as the first word
'''

import sys, getopt

def extract_senders_from_file(file_handle):
    
    sender_list = list()

    for line in file_handle:
        words = line.split()
        if len(words) > 2 and words[0] == 'From':
            sender = words[1]
            print(sender)
            sender_list.append(sender)
    
    return sender_list
    
def main(argv):

    input_file = ''
    unix_options = "i:"
    gnu_options = ["inputfile="]

    try:
        arguments, leftovers = getopt.getopt(argv, unix_options, gnu_options)
    except getopt.GetoptError as err:
        # output error, and return with an error code
        print (str(err))
        print ("Exiting.")
        sys.exit(2)
    
    for current_argument, current_value in arguments:
        if current_argument in ('-i', '--inputfile'):
            input_file = current_value
    
    if input_file == '':
        print("No input file given as parameter.")
        input_file = input("Please insert input file: ")

    print("Using file", input_file, "as input file.")

    try:
        file_handle = open(input_file)
    except:
        print("No such file found.")
        sys.exit(2)

    senders = extract_senders_from_file(file_handle)

    print(("There were %i lines in the file with From as the first word.") % (len(senders)))

    return

if __name__ == "__main__":
    main(sys.argv[1:])
