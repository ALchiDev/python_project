#!/usr/bin/python3
import random
number = random.randint(2, 4)
if number > 0 and number < 4:
    print(number, "is positive")
elif number == 0:
    print(number, "is zero")
elif number == 4:
    print(number, "is positive and the Maxi")
else:
    print(number, "is negative")
