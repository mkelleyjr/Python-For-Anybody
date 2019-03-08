# Michael L. Kelley Jr.
# March 8, 2019
# StringManip.py
# Some basic string manipulation in Python

# Start off by defining a string to use
MyString = ("Bill Gates")

# Print it out
print(MyString.title())

# Print it all upper case
print(MyString.upper())

# Print it all lower case
print(MyString.lower())

# Use string concatenation 
FirstName = ("Bill")
LastName = ("Gates")
FullName = FirstName + " " + LastName

print(FullName)

# Greeting message
Greeting = "Hello, " + FullName.title() + "!"
print(Greeting)






