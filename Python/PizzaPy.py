# Michael L. Kelley Jr.
# March 26, 2019
# PizzaPy.Py 

# Calculate how many pizzas to order for a party
# Assume for every 1.5 people, we will need 1 whole pizza

student_number = input("How many students will there be: ")

students_int = int(student_number)

# We assume that for every 1.5 students, you will need a whole pizza
# We add 1 pizza on the end to account for spares 
pizza_count = (students_int/1.5) + 1 

print("You will need", pizza_count, "pizzas")

