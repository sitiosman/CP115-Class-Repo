import random

# Takes the student's class name from the user
class_name = input("Enter your class name:")

# Generates a random number and displays class information
random_number = random.randint(1, 100)
print(f"Class Name: {class_name}")
print(f"Random Number: {random_number}")
