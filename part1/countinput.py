"""Author: Joe Ferber
Created: Sept. 11, 2026
Count characters other than spaces, periods, commas, and exclamation points.
"""


def countchars(st):
    count = 0
    for char in st:
        # Count the character if it is not one of the four skipped characters.
        if char not in " .!,":
            count += 1
    return count


# Black-box tests check examples with different kinds of text.
assert countchars("Listen, Mr. Jones, calm down.") == 21
assert countchars("r2?") == 3
assert countchars("Hello, world!") == 10
assert countchars("\t\n?") == 3

# Clear-box tests check an empty loop and both choices inside the loop.
assert countchars("") == 0
assert countchars(" .!,") == 0
assert countchars("abc") == 3

if __name__ == "__main__":
    print(countchars(input("Enter a string: ")))
