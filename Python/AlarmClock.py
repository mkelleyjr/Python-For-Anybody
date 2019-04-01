# Michael L. Kelley Jr.
# April 1, 2019
# AlarmClock.py

# Basic example of an if-else alarm AlarmClock

import time

# Get the current time 
current_time = time.localtime()

hour = current_time.tm_hour
minute = current_time.tm_min

# Define when you want to wake up with hour/minute 
wake_up = (hour > 7) or (hour == 7 and minute > 29)

# Let the user know if they should wake up or sleep with an if-else statement 
if wake_up:
    print("Wake up!!!!!")

else:
    print("You can sleep")

    