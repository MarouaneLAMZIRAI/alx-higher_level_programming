#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
last_digit = int(str(number)[-1])
to_be_printed = "Last digit of "+ str(number) + " is "+ str(last_digit)

if last_digit > 5 :
    to_be_printed = to_be_printed + " and is greater than 5"
elif last_digit == 0 :
    to_be_printed = to_be_printed + " and is 0"
elif last_digit < 6 :
    to_be_printed = to_be_printed + " and is less than 6 and not 0"
    
print(to_be_printed)
