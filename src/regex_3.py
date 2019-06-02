'''
Exercise 3: Finding Numbers in a Haystack

In this assignment you will read through and parse a file with text and numbers. 
You will extract all the numbers in the file and compute the sum of the numbers.

*Data Files*
We provide two files for this assignment. 
One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.

Sample data: http://py4e-data.dr-chuck.net/regex_sum_42.txt (There are 90 values with a sum=445833)
Actual data: http://py4e-data.dr-chuck.net/regex_sum_231755.txt (There are 91 values and the sum ends with 940)
These links open in a new window. Make sure to save the file into the same folder as you will be writing your Python program. 
Note: Each student will have a distinct data file for the assignment - so only use your own data file for analysis.

*Data Format*
The file contains much of the text from the introduction of the textbook except that random numbers are inserted throughout the text. 
Here is a sample of the output you might see:

Why should you learn to write programs? 7746
12 1929 8827
Writing programs (or programming) is a very creative 
7 and rewarding activity.  You can write programs for 
many reasons, ranging from making your living to solving
8837 a difficult data analysis problem to having fun to helping 128
someone else solve a problem.  This book assumes that 
everyone needs to know how to program ...
The sum for the sample text above is 27486. The numbers can appear anywhere in the line. There can be any number of numbers in each line (including none).

Handling The Data
The basic outline of this problem is to read the file, look for integers using the re.findall(), 
looking for a regular expression of '[0-9]+' and then converting the extracted strings to integers and summing up the integers.
'''

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import sys
import re

def main():
    url = get_url()
    ssl_context = set_ssl_context()
    html = open_url_to_html(url, ssl_context)
    soup = open_html_to_soup(html)
    (number_count, number_sum) = extract_numbers_from_page(soup)
    print_results(number_count, number_sum)
    return

def get_url():
    url = input('Enter URL: ')
    return url

def set_ssl_context():
    # Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    return ctx

def open_url_to_html(url, ssl_context):
    try:
        html = urllib.request.urlopen(url, context=ssl_context).read()
    except:
        print("Unable to open URL")
        sys.exit(2)
    
    return html

def open_html_to_soup(html_document):
    soup = BeautifulSoup(html_document, 'html.parser')
    return soup

def extract_numbers_from_page(html_soup):
    text = html_soup.get_text()
    number_regexp = r'[0-9]+'

    number_count = 0
    number_sum = 0
    numbers = list()
    
    numbers = re.findall(number_regexp, text)

    for number in numbers:
        number = int(number)
        number_count += 1
        number_sum += number
    
    return (number_count, number_sum)

def print_results(number_count, number_sum):
    print('Count:', number_count)
    print('Sum:', number_sum)

if __name__ == "__main__":
    main()