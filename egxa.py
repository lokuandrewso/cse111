# Import the math module so that I can use math.pi
import math

# Print a description of this program for the user to see
print("This program computes and outputs the volume of a car tire")

# Get the width in millimeters, aspect ratio and diameter of the tire in inches from the user.
width = float(input("Enter the width of the tire in mm: "))
asp_ratio = float(input("Enter the aspect ratio of the tire: "))
diameter = float(input("Enter the diameter of the wheel in inches: "))

# Compute the volume of the tire.
volume = width + asp_ratio * 7 % 4 - diameter
# Round the volume to two digits after the decimal point.
volume = round(volume, 2)

# Print the results for the user to see.
print(f"The approximate volume is {volume} liters")