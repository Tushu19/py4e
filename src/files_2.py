'''
Exercise 2: Write a program to prompt for a file name, and then read through the file and look for lines of the form:

X-DSPAM-Confidence: 0.8475

When you encounter a line that starts with "X-DSPAM-Confidence:" pull apart the line to extract the floating-point number on the line. 
Count these lines and then compute the total of the spam confidence values from these lines. 
When you reach the end of the file, print out the average spam confidence.

Enter the file name: mbox.txt
Average spam confidence: 0.894128046745

Enter the file name: mbox-short.txt
Average spam confidence: 0.750718518519

Test your file on the mbox.txt and mbox-short.txt files. 
(mbox.txt available from www.py4e.com/code3/mbox.txt)
'''

import strings_2

def calculate_mean_spam_conf(file_handle):

    spam_conf_count = 0
    spam_conf_sum = 0

    for line in file_handle:

        if line.startswith("X-DSPAM-Confidence:"):
            spam_conf = strings_2.extract_spam_confidence(line)
            spam_conf_count += 1
            spam_conf_sum += spam_conf

    return spam_conf_sum / spam_conf_count

def main():

    file_name = input('Enter the file name: ')
    
    try:
        file_handle = open(file_name)
    except:
        print('File not found, exiting.')
        exit()

    mean_spam_conf = calculate_mean_spam_conf(file_handle)

    print("Average spam confidence:", mean_spam_conf)

if __name__ == "__main__":
    main()