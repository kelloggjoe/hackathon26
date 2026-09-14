"""Author: Joe Ferber
Created: Sept. 11, 2026
Find the ticket amount based on the driving speed and speed limit.
"""

limit = int(input())
speed = int(input())
# Find how far the driving speed is above or below the limit.
difference = speed - limit

# Choose the ticket amount for this speed range.
if difference <= -10:
    ticket = 50
elif difference <= 5:
    ticket = 0
elif difference <= 20:
    ticket = 75
elif difference <= 40:
    ticket = 150
else:
    ticket = 300

print(ticket)
