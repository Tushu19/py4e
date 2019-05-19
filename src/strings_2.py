'''
Exercise 5: Take the following Python code that stores a string: string'X-DSPAM-Confidence:0.8475'
Use find and string slicing to extract the portion of the string after the colon character. 
Then use the float function to convert the extracted string into a floating point number.
'''

def extract_spam_confidence(spam_confidence_line):

    # Spam confidence lines are of format 'X-DSPAM-Confidence:    0.8475'
    # Amount of whitespace could vary

    # Remove whitespace
    spam_confidence_line = spam_confidence_line.strip()

    # Find colon
    colon_loc = spam_confidence_line.find(':')

    # Extract value up to end of line
    spam_confidence_value = spam_confidence_line[colon_loc+1:]

    # Convert to float
    spam_confidence_value = float(spam_confidence_value)

    return(spam_confidence_value)

def main():
    string = 'X-DSPAM-Confidence:    0.8475'
    spam_confidence = extract_spam_confidence(string)
    print(spam_confidence)

if __name__ == "__main__":
    main()