# Activity 3
import math
# Getting the diameter of the circle from the user
Diameter = float(input("Enter the diameter of the circle: "))
# Calculating the radius
Radius = Diameter / 2
# determining the height of the cylinder
Height = float(input("Enter the height of the cylinder: "))
# Calculating the volume of the cylinder
Pi_Rounded = round(math.pi, 2)
Volume = Pi_Rounded * (Radius ** 2) * Height
# Rounding the volume to 2 decimal places
Volume_Rounded = round(Volume, 2)
# Displaying the result
print(f"The volume of the cylinder is: {Volume_Rounded}")
