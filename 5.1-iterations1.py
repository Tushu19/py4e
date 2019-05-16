'''
Exercise 1: Write a program which repeatedly reads numbers until the user enters "done". 
Once "done" is entered, print out the total, count, and average of the numbers. 
If the user enters anything other than a number, detect their mistake using try and except and print an error message and skip to the next number.
'''

def main():

    sum = 0
    count = 0

    while True:

        number_input = input('Please insert a number, or type \'done\' if you are ready to finish: ')
        
        if number_input == "done":
            break

        else:

            try:
                number_input = float(number_input)
            except:
                print('Input not a number or \'done\'.')
                continue
            
            count += 1
            sum += number_input
    
    print('Final sum: ', sum)
    print('Final count:', count)
    print('Final average:', sum/count)

main()