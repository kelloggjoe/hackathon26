"""Author: Joe Ferber
Created: Sept. 11, 2026
Check the Part 1 programs with sample inputs and boundary values.
"""

import subprocess
import sys
from pathlib import Path

# These imports also run the tests inside the two files.
import countinput
import stocktrading


def run(filename, data):
    path = Path(__file__).parent / filename
    # Run the file with test input and save its printed output.
    result = subprocess.run(
        [sys.executable, str(path)], input=data, text=True,
        capture_output=True, check=True
    )
    return result.stdout


# Check the values on both sides of each ticket cutoff.
for difference, ticket in [
    (-30, 50), (-10, 50), (-9, 0), (0, 0), (5, 0), (6, 75),
    (20, 75), (21, 150), (40, 150), (41, 300), (100, 300)
]:
    assert run("speedingticket.py", f"35\n{35 + difference}\n") == f"{ticket}\n"

# Check the sample, temperature cutoffs, and different types of days.
for temps, heating, cooling in [
    ([33, 90, 98, 66, 22, -460], 2, 2),
    ([-459, 59, 60, 80, 81, -460], 2, 1),
    ([-460], 0, 0),
    ([-500], 0, 0),
    ([60, 70, 80, -460], 0, 0),
    ([0, 59, -460], 2, 0),
    ([81, 100, -460], 0, 2)
]:
    data = "\n".join(str(temp) for temp in temps) + "\n"
    # Each temperature entered should display one prompt.
    expected = "Enter the average daily temperature: " * len(temps)
    expected += f"Heating days: {heating}\nCooling days: {cooling}\n"
    assert run("heatingcooling.py", data) == expected

assert run("countinput.py", "Hello, world!\n") == "Enter a string: 10\n"
print("All tests passed.")
