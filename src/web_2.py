'''
Extracting Data from JSON

In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/json2.py. 
The program will 
* prompt for a URL, 
* read the JSON data from that URL using urllib 
* and then parse and extract the comment counts from the JSON data, 
* compute the sum of the numbers in the file 
* and enter the sum below.

We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.

Sample data: http://py4e-data.dr-chuck.net/comments_42.json (Sum=2553)
Actual data: http://py4e-data.dr-chuck.net/comments_231760.json (Sum ends with 19)
You do not need to save these files to your folder since your program will read the data directly from the URL. Note: Each student will have a distinct data url for the assignment - so only use your own data url for analysis.

Data Format
The data consists of a number of names and comment counts in JSON as follows:

{
  comments: [
    {
      name: "Matthias"
      count: 97
    },
    {
      name: "Geomer"
      count: 97
    }
    ...
  ]
}
The closest sample code that shows how to parse JSON and extract a list is json2.py. You might also want to look at geoxml.py to see how to prompt for a URL and retrieve data from a URL.

Sample Execution

$ python3 solution.py
Enter location: http://py4e-data.dr-chuck.net/comments_42.json
Retrieving http://py4e-data.dr-chuck.net/comments_42.json
Retrieved 2733 characters
Count: 50
Sum: 2...
'''

import urllib.request, urllib.parse, urllib.error
import json
import ssl
import sys,getopt

def main(argv):
    url_handle = open_url(argv)
    url_data_string = get_data_from_url(url_handle)
    json_doc = read_string_to_json(url_data_string)
    comment_list = extract_comments_from_json(json_doc)
    results_dict = get_metrics_from_comments(comment_list)
    print_results(results_dict)
    return

def open_url(command_line_arguments):
    unix_options = "u:"
    gnu_options = ["url="]

    url_handle = None
    input_url = None

    ssl_context = set_ssl_context_to_ignore()

    try:
        arguments, leftovers = getopt.getopt(command_line_arguments, unix_options, gnu_options)
    except getopt.GetoptError as err:
        # output error, and return with an error code
        print (str(err))
        print ("Exiting.")
        sys.exit(2)
    
    for current_argument, current_value in arguments:
        if current_argument in ('-u', '--url'):
            input_url = current_value
    
    if not input_url:
        input_url = input("Enter location: ")

    print("Retrieving", input_url)

    try:
        url_handle = urllib.request.urlopen(input_url, context=ssl_context)
    except:
        print("No such URL found.")
        sys.exit(2)

    return url_handle

def set_ssl_context_to_ignore():
    # Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    return ctx

def get_data_from_url(url_handle):
    url_data = url_handle.read()
    print('Retrieved', len(url_data), 'characters')
    return url_data

def read_string_to_json(data_string):
    json_doc = json.loads(data_string)
    return json_doc

def extract_comments_from_json(json_doc):
    comments = list()
    comments = json_doc['comments']
    return comments

def get_metrics_from_comments(comment_list):
    comment_count = 0
    comment_sum = 0
    
    for comment in comment_list:
        comment_count += 1
        comment_sum += comment['count']

    results_dict = dict()
    results_dict['Count'] = comment_count
    results_dict['Sum'] = comment_sum

    return results_dict

def print_results(results_dict):
    for item in results_dict.items():
        print ('%s: %s' % (item[0], item[1]))
    return

if __name__ == "__main__":
    main(sys.argv[1:])
