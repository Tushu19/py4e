'''
Exercise 1: Write a function called chop that takes a list and modifies it, removing the first and last elements, and returns None. 
Then write a function called middle that takes a list and returns a new list that contains all but the first and last elements.
'''

def chop(chop_list):
    # Function that modifies a list by removing the first and last elements

    # Remove last element
    chop_list.pop()

    # Remove first element
    chop_list.pop(0)

    # Return None as list is modified as a 
    return None

def middle(middle_list):
    # Function that returns a new list without the first and last elements
    # of list given as parameter

    return middle_list[1:len(middle_list)-2]

def main():
    # Chopping
    chop_list = input("Enter list to chop: ")
    
    chop(chop_list)
    print(chop_list) # This works
    
    #chopped_list = chop(chop_list)
    #print(chopped_list) # This doesn't

    # Middling
    middle_list = input("Enter list to middle: ")

    middle(middle_list)
    print(middle_list) # This returns the original list

    middled_list = middle_list(middle_list)
    print(middled_list) # This returns the modified list

    return

if __name__ == "__main__":
    main()