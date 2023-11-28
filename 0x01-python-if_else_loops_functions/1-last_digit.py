#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lst_dgit = abs(number) % 10
if number < 0:
    lst_dgit = -lst_dgit

if lst_dgit > 5:
    print(f"Last digit of {number} is {lst_dgit} and is greater than 5")
elif lst_dgit < 6 and lst_dgit != 0:
    print(f"Last digit of {number} is {lst_dgit} and is less than 6 and not 0")
else:
    print(f"Last digit of {number} is {lst_dgit} and is 0")
