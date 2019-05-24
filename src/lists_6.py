'''
Exercise 6: Rewrite the program that prompts the user for a list of numbers and prints out the maximum and minimum of the numbers at the end when the user enters "done". 
Write the program to store the numbers the user enters in a list and use the max() and min() functions to compute the maximum and minimum numbers after the loop completes.

Enter a number: 6
Enter a number: 2
Enter a number: 9
Enter a number: 3
Enter a number: 5
Enter a number: done
Maximum: 9.0
Minimum: 2.0
'''

def prompt_user_for_numbers():
    
    numbers = list()
    user_input = 0

    while True:

        user_input = input("Enter a number: ")

        if user_input in ('done', 'Done'):
            break
        
        try:
            input_number = int(user_input)
        except:
            print("Not a number.")
            continue

        numbers.append(input_number)
    
    return numbers

def print_results(number_list):

    print("Maximum:", max(number_list))
    print("Minimum:", min(number_list))
    return

def main():

    number_list = prompt_user_for_numbers()

    print_results(number_list)

    return

if __name__ == "__main__":
    main()