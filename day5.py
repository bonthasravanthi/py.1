# Write a Python function named calculate_sum that takes no arguments and returns the sum of two variables: x and y.
# Define x and y within the global scope and assign them integer values of 5 and 10 respectively.
# Within the calculate_sum function, define a local variable z and assign it the value of x + y.
# Return z from the calculate_sum function and print the result when the function is called.
# Execute the function and verify that the output is correct, demonstrating the correct application of scope in accessing variables.

x=5
y=10
def calculate_sum():
    z=x+y
    return z
print(calculate_sum())


# Create a global variable a = 20.
# Write a function display_value() that:
# Takes no arguments.
# Creates a local variable b = 10.
# Returns the sum of a and b.
# Print the result

a=20
def display_value():
    b=10
    c=a+b
    return c
print(display_value())

# Create two global variables
# Write a function user_info() that:
# Takes no arguments.
# Creates a local variable message.
# Stores "Sravanthi is 21 years old" in message.
# Returns message.
# Print the result.

name="python"
course="data science"
def user_course():
    message="python is a part of data science"
    return message
print(user_course())

# Create a global variable:
# num = 50
# Write a function square_num() that:
# Takes no arguments.
# Creates a local variable result.
# Stores the square of num in result.
# Returns result.

num=50
def square_num():
    result=num**2
    return result
print(square_num())


# Create global variables:
# length = 8
# width = 4
# Write a function calculate_area() that:
# Takes no arguments.
# Creates a local variable area.
# Calculates the area of the rectangle.
# Returns area.

length=8
width=4
def calculate_area():
    area=length*width
    return area
print(calculate_area())

#addition of two numbers

def add_two_numbers():
    a=20
    b=30
    return a+b
print(add_two_numbers())

# x = 10
# def display():
#     print(x)
# display()


# Write a program:
# Create a global variable num = 100
# Create a function show_num()
# Inside the function, print num
# Call the function

num=100
def show_num():
    print(num)
show_num()


# Create a global variable name = "Python"
# Create a function show_name()
# Inside the function, create a local variable course = "Data Science"
# Print both variables inside the function

name="sql"
def show_name():
    course="data analyst"
    print(name,course)
show_name()

