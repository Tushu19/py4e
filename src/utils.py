'''
Useful, often-repeated functions
'''

import sys, getopt


def open_file_to_handle(command_line_arguments):
    input_file = ''
    unix_options = "i:"
    gnu_options = ["inputfile="]
    file_handle = None

    try:
        arguments, leftovers = getopt.getopt(command_line_arguments, unix_options, gnu_options)
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

    try:
        file_handle = open(input_file)
    except:
        print("No such file found.")
        sys.exit(2)

    print("Using file", input_file, "as input.")

    return file_handle


def is_proper_sender_line(email_line_string):
    word_list = email_line_string.split()
    return (len(word_list) > 2 and word_list[0] == "From") 