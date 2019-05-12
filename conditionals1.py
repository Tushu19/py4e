'''
3.1 Write a program to prompt the user for hours and rate per hour using input to compute gross pay. 
Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours. 
Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). 
You should use input to read a string and float() to convert the string to a number. 
Do not worry about error checking the user input - assume the user types numbers properly.
'''

hours_worked = input('Please enter total number of hours worked: ')
hours_worked = float(hours_worked)

rate = input('Please enter hourly rate: ')
rate = float(rate)

gross_pay = 0

if hours_worked <= 40:
    gross_pay = hours_worked * rate
else:
    hours_normaltime = 40
    hours_overtime = hours_worked - hours_normaltime
    gross_pay = hours_normaltime * rate + hours_overtime * rate * 1.5

print(gross_pay)