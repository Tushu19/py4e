'''
Exercise 2: Write a program to look for lines of the form:

New Revision: 39772

Extract the number from each of the lines using a regular expression and the findall() method. Compute the average of the numbers and print out the average.

Enter file:mbox.txt
38444.0323119

Enter file:mbox-short.txt
39756.9259259
'''
import sys, re, utils


def extract_newrevision_number(text_line):
    line_results_dict = dict()
    newrevision_regex = "^New Revision:? ([0-9]+)"
    found_matches = re.findall(newrevision_regex, text_line)
    if len(found_matches) > 0:
        for match in found_matches:
            line_results_dict[match] = line_results_dict.get(match, 0) + 1
    
    return line_results_dict


def main(arguments):
    file_handle = utils.open_file_to_handle(arguments)
    results_dict = utils.process_text_file_to_dict(file_handle, extract_newrevision_number)
    
    revision_number_sum = 0
    revision_number_count = 0

    for revision_number, occurrences in results_dict.items():
        try:
            revision_number = int(revision_number)
        except:
            print('Not a number:', revision_number)
            continue

        revision_number_sum += revision_number
        revision_number_count += occurrences

    print("Number of New Revisions:", revision_number_count)
    print("Average revision number:", revision_number_sum/revision_number_count)

    return


if __name__ == "__main__":
    main(sys.argv[1:])