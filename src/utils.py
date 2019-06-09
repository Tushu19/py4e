'''
Useful, often-repeated functions
'''

import sys, getopt, sqlite3
import xml.etree.ElementTree as ET

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


def process_sender_lines_to_dict(email_file, process_line_function):
    result_dictionary = dict()

    for line in email_file:
        if is_proper_sender_line(line):
            metric_key = process_line_function(line)
            result_dictionary[metric_key] = result_dictionary.get(metric_key, 0) + 1
    
    return result_dictionary


def process_text_file_to_dict(text_file, process_line_to_dict_function):
    result_dict = dict()
    
    for line in text_file:
        line_results_dict = process_line_to_dict_function(line)
    
        for key, value in line_results_dict.items():
            result_dict[key] = result_dict.get(key, 0) + value
    
    return result_dict


def sort_dict_by_keys(input_dict, use_reverse_order = False):
    sorted_by_key = sorted([(key, value) for key, value in input_dict.items()], reverse = use_reverse_order)
    return dict(sorted_by_key)


def sort_dict_by_values(input_dict, use_reverse_order = False):
    sorted_by_value = sorted([(value, key) for key, value in input_dict.items()], reverse = use_reverse_order)
    return dict([(key, value) for value, key in sorted_by_value])
    

def print_dict_by_line(dict_to_print):
    for key, value in dict_to_print.items():
        print(key, value)

def create_db_connection(db_address):
    connection = sqlite3.connect(db_address)
    cursor = connection.cursor()
    return (connection, cursor)

def open_xml(xml_handle):
    xml_data = xml_handle.read()
    print('Retrieved', len(xml_data), 'characters')
    root = ET.fromstring(xml_data)
    return root