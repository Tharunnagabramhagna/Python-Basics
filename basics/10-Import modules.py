import random
import math
import time
import os
import datetime
import sys
import calendar

# 1)Get a random number

random_number = random.randint(1, 10)
print(f"Random Number is: {random_number}")

# 2)choose a random element from a list

fruits = ["apple", "cherry", "banana", "orange"]
random_number = random.choice(fruits)
print(f"Random fruit is: {random_number}")

# 3)shuffle the list

random.shuffle(fruits)
print(f"shuffled list is: {fruits}")

# 4)math module

print(f"square root of 81: {int(math.sqrt(81))}")
print(f"ceiling of 5.3 : {math.ceil(5.3)}")
print(f"floor of 7.8: {math.floor(7.8)}")
print(f"2 raised to power 7 is: {int(math.pow(2, 7))}")
print(f"value of pi: {math.pi}")

# 5)Time module
print("waiting for 2 seconds...")
time.sleep(2)
print("Done!")

# 6)OS module

current_directory = os.getcwd()
print(f"Current Directory is: {current_directory}")
print(f"List of files: {os.listdir('.')}")

# 7)Datetime module

current_time = datetime.datetime.now()
print(f"Current Date and Time: {current_time}")
print(f"Today's Date: {datetime.date.today()}")
print(f"Current year: {datetime.date.today().year}")
print(f"Current month: {datetime.date.today().month}")

# 8)System module

print(f"Python version: {sys.version}")
# eg:- win32 for windows,darwin for macbook,linux for linux laptop
print(f"platform: {sys.platform}")

# 9)Calendar module
yy = int(input("Enter the current year: "))
mm = int(input("Enter the current month: "))

print(calendar.month(yy, mm))  # prints the current month calendar

# checks if the current year is a leap year or not
print(calendar.isleap(yy))

print(calendar.calendar(yy))  # prints the whole calendar of the current year
