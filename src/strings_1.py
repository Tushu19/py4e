'''
Exercise 1: Write a while loop that starts at the last character in the string and works its way backwards to the first character in the string, 
printing each letter on a separate line, except backwards.
'''

string = input('Insert string: ')

iterator = len(string) - 1

while iterator >= 0:

    print(string[iterator])
    iterator -= 1