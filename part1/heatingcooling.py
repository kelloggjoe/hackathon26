"""Author: Joe Ferber
Created: Sept. 11, 2026
Count heating and cooling days from daily temperatures.
"""

heating = 0
cooling = 0

while True:
    temp = int(input("Enter the average daily temperature: "))
    # Stop before counting the ending value as a day.
    if temp < -459:
        break
    # Count cold days as heating days and hot days as cooling days.
    if temp < 60:
        heating += 1
    elif temp > 80:
        cooling += 1

print("Heating days:", heating)
print("Cooling days:", cooling)
