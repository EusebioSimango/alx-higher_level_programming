#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastDigit = int(str(number)[-1])
print(f"Last digit of {number} is {lastDigit} and is", end=" ")
if (lastDigit > 5):
    print("greater than 5")
elif ((lastDigit < 6) and (lastDigit != 0)):
    print("less than 6 and not 0")
else:
    print("zero")
