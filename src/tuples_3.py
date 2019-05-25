'''
Exercise 3: Write a program that reads a file and prints the letters in decreasing order of frequency. 
Your program should convert all the input to lower case and only count the letters a-z. 
Your program should not count spaces, digits, punctuation, or anything other than the letters a-z. 
Find text samples from several different languages and see how letter frequency varies between languages. 
Compare your results with the tables at https://wikipedia.org/wiki/Letter_frequencies.
'''
import sys, utils, string

def count_letters_from_text_line(text_line):
    line_result_dict = dict()
    letters = text_line.translate(str.maketrans('', '', (string.punctuation + string.whitespace + string.digits)))
    letters_lowercase = letters.lower()

    for letter in letters_lowercase:
        line_result_dict[letter] = line_result_dict.get(letter, 0) + 1

#    DEBUG
#    print(text_line.strip())
#    print(line_result_dict)
#    /DEBUG

    return line_result_dict


def main(arguments):
    text_file_handle = utils.open_file_to_handle(arguments)
    result_dict = utils.process_text_file_to_dict(text_file_handle, count_letters_from_text_line)
    sorted_by_values = utils.sort_dict_by_values(result_dict, use_reverse_order=True)
    utils.print_dict_by_line(sorted_by_values)
    return

if __name__ == "__main__":
    main(sys.argv[1:])