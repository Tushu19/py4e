'''
4.6 Write a program to prompt the user for hours and rate per hour using input to compute gross pay. 
Pay should be the normal rate for hours up to 40 and time-and-a-half for the hourly rate for all hours worked above 40 hours. 
Put the logic to do the computation of pay in a function called computepay() and use the function to do the computation. 
The function should return a value. 
Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). 
You should use input to read a string and float() to convert the string to a number. 
Do not worry about error checking the user input unless you want to - you can assume the user types numbers properly. 
Do not name your variable sum or use the sum() function.
'''

def computepay(hours_worked, rate_per_hour):
    
    gross_pay = 0

    if hours_worked <= 40:
        gross_pay = hours_worked * rate_per_hour
    else:
        hours_normaltime = 40
        hours_overtime = hours_worked - hours_normaltime
        gross_pay = hours_normaltime * rate_per_hour + hours_overtime * rate_per_hour * 1.5

    return gross_pay

hours_worked = input('Please input number of hours worked: ')
hours_worked = float(hours_worked)

rate_per_hour = input('Please input rate per hour: ')
rate_per_hour = float(rate_per_hour)

print(computepay(hours_worked, rate_per_hour))