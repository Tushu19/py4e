'''
Exercise 1: Write a program to read through a file and print the contents of the file (line by line) all in upper case. 
Executing the program will look as follows:

python shout.py
Enter a file name: mbox-short.txt
FROM STEPHEN.MARQUARD@UCT.AC.ZA SAT JAN  5 09:14:16 2008
RETURN-PATH: <POSTMASTER@COLLAB.SAKAIPROJECT.ORG>
RECEIVED: FROM MURDER (MAIL.UMICH.EDU [141.211.14.90])
     BY FRANKENSTEIN.MAIL.UMICH.EDU (CYRUS V2.3.8) WITH LMTPA;
     SAT, 05 JAN 2008 09:14:16 -0500

You can download the file from www.py4e.com/code3/mbox-short.txt
'''

def text_file_to_upper_case(file_name):

    # Try to open file for reading
    try:
        file_handle = open(file_name)
    except:
        # Exit if not found
        print("File not found, exiting.")
        exit()
    
    # If file is found, read line by line and print in upper case
    # Break at 50 lines to limit printing

    counter = 0
    for line in file_handle:
        line = line.rstrip()
        print(line.upper())
        counter += 1
        if counter > 50: break

def main():
    file_name = input("Please input file name: ")
    text_file_to_upper_case(file_name)

main()