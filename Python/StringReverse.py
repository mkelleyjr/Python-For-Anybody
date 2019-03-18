# Michael L. Kelley Jr.
# March 18, 2019
# StringReverse.py

# You can reverse strings and lists in Python

# Function for string reverse
def reverse(string):
    string = "".join(reversed(string))
    return string

MyString = "Michael"
print("My string is: " + MyString)

# Now, we will reverse it and print the reversed string
print("The reversed string is ", end ="")
print(reverse(MyString))


