# Ask the user for input and store in variables
name = input("Enter your name:")
age = int(input("Enter your age:"))
course_code = input("Enter your course code:")

# Display the collected information
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Course Code: {course_code}")

# Show the data types of the collected information
print(f"Data type of name: {type(name)}")
print(f"Data type of age: {type(age)}")
print(f"Data type of course code: {type(course_code)}")
