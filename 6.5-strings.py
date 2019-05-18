'''
Exercise 5: Take the following Python code that stores a string: string'X-DSPAM-Confidence:0.8475'
Use find and string slicing to extract the portion of the string after the colon character. 
Then use the float function to convert the extracted string into a floating point number.
'''

def main():
    
    string = 'X-DSPAM-Confidence:    0.8475'

    # Remove whitespace
    string = string.strip(' ')

    colon_loc = string.find(':')

    value = string[colon_loc+1:]

    value = float(value)

    print(value)

main()