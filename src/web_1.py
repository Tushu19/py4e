'''
Extracting Data from XML

In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/geoxml.py. 
The program will prompt for a URL, read the XML data from that URL using urllib and then parse and extract the comment counts from the XML data, compute the sum of the numbers in the file.

We provide two files for this assignment. 
One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.

Sample data: http://py4e-data.dr-chuck.net/comments_42.xml (Sum=2553)
Actual data: http://py4e-data.dr-chuck.net/comments_231759.xml (Sum ends with 26)
You do not need to save these files to your folder since your program will read the data directly from the URL. 
Note: Each student will have a distinct data url for the assignment - so only use your own data url for analysis.

Data Format and Approach
The data consists of a number of names and comment counts in XML as follows:

<comment>
  <name>Matthias</name>
  <count>97</count>
</comment>

You are to look through all the <comment> tags and find the <count> values sum the numbers. 
The closest sample code that shows how to parse XML is geoxml.py. 
But since the nesting of the elements in our data is different than the data we are parsing in that sample code you will have to make real changes to the code.
To make the code a little simpler, you can use an XPath selector string to look through the entire tree of XML for any tag named 'count' with the following line of code:

counts = tree.findall('.//count')

Take a look at the Python ElementTree documentation and look for the supported XPath syntax for details. 
You could also work from the top of the XML down to the comments node and then loop through the child nodes of the comments node.

Sample Execution

$ python3 solution.py
Enter location: http://py4e-data.dr-chuck.net/comments_42.xml
Retrieving http://py4e-data.dr-chuck.net/comments_42.xml
Retrieved 4189 characters
Count: 50
Sum: 2...
'''

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl
import sys,getopt

def main(argv):
    url_handle = open_url(argv)
    xml_tree_root = open_xml(url_handle)
    (commenter_count, total_comments) = get_comment_metrics(xml_tree_root)
    print('Count:', commenter_count)
    print('Sum', total_comments)
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

def open_xml(url_handle):
    xml_data = url_handle.read()
    print('Retrieved', len(xml_data), 'characters')
    root = ET.fromstring(xml_data)
    return root

def get_comment_metrics(xml_elementtree_root):
    comment_counts = xml_elementtree_root.findall('.//count')

    commenter_count = 0
    total_comments = 0
    
    for count in comment_counts:
        try:
            count_int = int(count.text)
        except:
            print('Invalid number:', count)
            sys.exit(2)

        commenter_count += 1
        total_comments += count_int

    return (commenter_count, total_comments)

if __name__ == "__main__":
    main(sys.argv[1:])