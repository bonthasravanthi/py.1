# Write a list comprehension to generate numbers from 1 to 10.
print([x for x in range(1,11)] )

# # Create a list of squares of numbers from 1 to 10.
print([x**2 for x in range (1,11)])

# Write a list comprehension to extract only even numbers from a list:
even=[x%2==0 for x in range(1,11)]
print(even) # it prints boolean

even=[x for x in range(1,20)if x%2==0]
print(even)

# Conditional Comprehension
# Create a list of numbers divisible by 3 from 1 to 30.
divisible=[x for x in range(1,30) if x%3==0]
print(divisible)

# Convert all negative numbers in a list to positive using comprehension:
nums=[x for x in range(-1,-20,-1) ]
print([abs(x) for x in nums])


# Create a list of first letters of each word:

words = ["python", "java", "sql", "html"]
print([ x[0] for x  in words])
print([x[2] for x in words])


# Convert all words to uppercase using list comprehension.
words = ["python", "java", "sql", "html"]
print([x.upper() for x in words])

# Dictionary Comprehension Questions
# Create a dictionary where keys are numbers from 1 to 5 and values are their squares.
dic={x:x**2 for x in range(1,5)}
print(dic)


# Create a dictionary with names as keys and their lengths as values.

name={"ram","hari","harsha","sai"}
print({x:len(x) for x in name})

# Swap keys and values in a dictionary using comprehension:
d = {"a": 1, "b": 2, "c": 3}
swapped={v:k for k,v in d.items()}
print(swapped)

# Set Comprehension Questions
# Create a set of unique squares from numbers 1 to 10.
print({x**2 for x in range(1,11)})

# Remove duplicates from this list using set comprehension:
s=[1,1,3,4,5,6,6,7,8,9,9]
print({x for x in s})