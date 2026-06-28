# Write a program to handle ZeroDivisionError.
try:
    if 7/0:
        print("error")
except:
    print("failed but catches the error")

# Write a program to handle IndexError.
s=[1,2,3,4]
try:
    print(s[5])
except IndexError:
    print("index is out of range")


# Write a program to handle ValueError.

try:
    age=int(input("enter your age:"))
    print(age)
except ValueError:
    print("it is a value error")

# Write a program to handle multiple exceptions.
try:
    name = input("Enter your name: ")
    print(name[9])
except IndexError:
    print("IndexError occurred.")

try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print(result)
except ValueError:
    print("ValueError occurred.")
except ZeroDivisionError:
    print("Cannot divide by zero.")

try:
    x = int(input("Enter another number: "))
    print(x)
except ValueError:
    print("Invalid number.")
except Exception as error:
    print("Error:", error)


# Write a program using try, except, else, and finally.
try:
    num=int(input("enter a number:"))
    result=10/num
    print(result)
except ValueError:
    print("enter a valid number")

except ZeroDivisionError:
    print("cannot divide by zero")
else:
    print("successful")
finally:
    print("i always executes")



# Write a program to raise a custom exception.
class AgeError(Exception):
    pass

age = 18

try:
    if age < 20:
        raise AgeError("Not eligible")
    print("Eligible for vote")
except AgeError as error:
    print(error)

     
# Write a program to open a file safely using exception handling.

try:
    file=open("sample.text","r")
    print(file.read())
    file.close()
except FileNotFoundError:
    print("file not found")

# Write a program that asks the user for an integer and handles invalid input.
try:
    num=int(input("enter a number:"))
    print("number is valid:",num)
except ValueError:

    print("invalid input! please enter a integer")