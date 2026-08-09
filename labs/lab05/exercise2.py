import math

# Takes the radius of a circle from the user
radius = float(input("Enter the radius of the circle: "))

# Calculate the area and circumference of the circle
area = math.pi * (radius ** 2)
circumference = 2 * math.pi * radius

# Print the results
print(f"Area of the circle : {area}")
print(f"Circumference of the circle : {circumference}")


