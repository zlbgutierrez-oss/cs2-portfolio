import math

x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

x_difference = math.pow(x2 - x1, 2)
y_difference = math.pow(y2 - y1, 2)

distance = math.sqrt(x_difference + y_difference)

print(f"The distance between the two points is: {distance:.2f}")
 
# Reflection:
# Using the math library makes the program easier because I can use
# sqrt() and pow() instead of creating these mathematical calculations myself.
# Without these functions, I would need to write more complicated code to perform the same calculations.
