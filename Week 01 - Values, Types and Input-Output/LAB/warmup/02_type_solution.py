""" # BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.

value = input("Value: ")

print(value + 1)

"""

# input() will always output string but the print(value + 1) is asking for a calculation. therefore we have to convert the type of value that input gives us as shown below.

value = float(input("value: "))

print(value + 1)

# by putting the whole input function into the float function we change the type of variable that input gives us from string to float.