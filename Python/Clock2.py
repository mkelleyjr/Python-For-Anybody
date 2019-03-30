# Michael L. Kelley Jr.
# March 29, 2019
# Clock2Py.

# Version 2 of a time program. Return the current hour + minutes

import time

current_time = time.localtime()

hour = current_time.tm_hour
mins = current_time.tm_min

print("The current time is:", hour,":",mins)