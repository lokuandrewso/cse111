# Import the math module so that I can use math.pi
import math

# Print a description of this program for the user to see
print("This program computes and outputs the volume of a car tire")

# Get the width in millimeters, aspect ratio and diameter of the tire in inches from the user.
width = float(input("Enter the width of the tire in mm: "))
asp_ratio = float(input("Enter the aspect ratio of the tire: "))
diameter = float(input("Enter the diameter of the wheel in inches: "))

# Compute the volume of the tire.
volume = (math.pi * width**2 * asp_ratio * (width * asp_ratio + 2540 * diameter)) / 10000000000

# Round the volume to two digits after the decimal point.
volume = round(volume, 2)

# Print the results for the user to see.
print(f"The approximate volume is {volume} liters")

# Import the datetime module
from datetime import datetime

my_date = datetime.today()

date = my_date.date()
print(date)

#open a text file named volumes.txt
with open("volumes.txt", "at") as my_files:

    #Append the needed information for the user
    print(f"{date}, {width}, {asp_ratio}, {diameter}, {volume}", file=my_files)