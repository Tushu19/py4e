'''
Exercise 3: Following Links in Python

In this assignment you will write a Python program that expands on http://www.py4e.com/code3/urllinks.py. 
The program will use urllib to read the HTML from the data files below, 
extract the href= vaues from the anchor tags, 
scan for a tag that is in a particular position relative to the first name in the list, 
follow that link 
and repeat the process a number of times and report the last name you find.

We provide two files for this assignment. One is a sample file where we give you the name for your testing 
and the other is the actual data you need to process for the assignment

Sample problem: Start at http://py4e-data.dr-chuck.net/known_by_Fikret.html 
Find the link at position 3 (the first name is 1). Follow that link. Repeat this process 4 times. The answer is the last name that you retrieve.
Sequence of names: Fikret Montgomery Mhairade Butchi Anayah 
Last name in sequence: Anayah
Actual problem: Start at: http://py4e-data.dr-chuck.net/known_by_Alihaider.html 
Find the link at position 18 (the first name is 1). Follow that link. Repeat this process 7 times. The answer is the last name that you retrieve.
Hint: The first character of the name of the last page that you will load is: B
Strategy
The web pages tweak the height between the links and hide the page after a few seconds to make it difficult for you to do the assignment without writing a Python program. But frankly with a little effort and patience you can overcome these attempts to make it a little harder to complete the assignment without writing a Python program. But that is not the point. The point is to write a clever Python program to solve the program.

Sample execution

Here is a sample execution of a solution:

$ python3 solution.py
Enter URL: http://py4e-data.dr-chuck.net/known_by_Fikret.html
Enter count: 4
Enter position: 3
Retrieving: http://py4e-data.dr-chuck.net/known_by_Fikret.html
Retrieving: http://py4e-data.dr-chuck.net/known_by_Montgomery.html
Retrieving: http://py4e-data.dr-chuck.net/known_by_Mhairade.html
Retrieving: http://py4e-data.dr-chuck.net/known_by_Butchi.html
Retrieving: http://py4e-data.dr-chuck.net/known_by_Anayah.html
The answer to the assignment for this execution is "Anayah".
'''

# To run this, you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# Or download the file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import sys

def main():
    initial_url = get_url()
    (depth_count, position_in_links) = get_depth_and_position()
    find_name_at_depth_and_position(initial_url, depth_count, position_in_links)
    return

def get_url():
    url = input('Enter URL: ')
    return url

def get_depth_and_position():
    depth_count = 0
    position_in_links = 0

    depth_count = input('Enter count: ')

    try:
        depth_count = int(depth_count)
    except:
        print('Not a number.')
        sys.exit(2)
    
    position_in_links = input('Enter position: ')

    try:
        position_in_links = int(position_in_links)
    except:
        print("Not a number.")
        sys.exit(2)
    
    return (depth_count, position_in_links)

def find_name_at_depth_and_position(initial_url, depth_count, position_in_links):
    ssl_context = set_ignore_ssl_context()

    next_url = initial_url

    for step in range(0, depth_count):
        print('Retrieving:', next_url)
        html = open_url(next_url, ssl_context)
        soup = open_html_to_soup(html)
        (next_name, next_url) = retrieve_next_from_anchor_tags(soup, position_in_links)
    
    print('Retrieving:', next_url)
    print('The answer to the assignment for this execution is "%s".' % format(next_name))

    return next_name

def set_ignore_ssl_context():
    # Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    return ctx

def open_url(url, ssl_context):
    try:
        html = urllib.request.urlopen(url, context=ssl_context).read()
    except:
        print("Unable to open URL")
        sys.exit(2)
    
    return html

def open_html_to_soup(html_document):
    soup = BeautifulSoup(html_document, 'html.parser')
    return soup

def retrieve_next_from_anchor_tags(soup, position_in_links):
    anchor_tags = soup('a')

    next_url_tag = None

    try:
        next_url_tag = anchor_tags[position_in_links - 1]
    except:
        print('Too few links on current page to go to desired position in links.')
        sys.exit(2)
    
    next_url = next_url_tag.get('href', None)
    next_name = next_url_tag.contents[0]

    return (next_name, next_url)

if __name__ == "__main__":
    main()