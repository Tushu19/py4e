'''
5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. 
Once 'done' is entered, print out the largest and smallest of the numbers. 
If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number. 
Enter 7, 2, bob, 10, and 4 and match the output below ("Invalid input", "Maximum is 10", "Minimum is 2").
'''

def largestsmallestcalculator():

    smallest = None
    largest = None

    while True:

        number_input = input("Enter a number or type 'done' to finish: ")

        if number_input == 'done':
            break
        
        else:
            
            try:
                number_input = int(number_input)
            except:
                print("Invalid input")
                continue

            if smallest == None or number_input < smallest:
                smallest = number_input

            if largest == None or number_input > largest:
                largest = number_input
    
    print("Maximum is", largest)
    print("Minimum is", smallest)

def main():
    largestsmallestcalculator()

main()