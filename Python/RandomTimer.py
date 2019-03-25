# Michael L. Kelley Jr.
# March 25, 2019
# RandomTimer.py

# Generate a random timer in Python
# We will generate a time between 10-60 seconds, randomized

# Use these libraries 
import time
import random

print("Welcome to time program 1.0")

# Get a random amt of seconds
srand_time = random.randint(10, 60)

print("Timer now starting for: ", + srand_time)

# Start the timer 
time.sleep(srand_time)

print("Time is now up!")


