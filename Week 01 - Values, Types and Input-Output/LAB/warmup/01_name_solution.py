# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.

"""record_id = "R-004"

print(record_ID) """

#The problem with the original syntax is the defined variable is different from the declared variable. 
# Python is very case sensitive and because the syntax had "ID" instead of "id" python couldn't recognise it.

# we can fix this by using the correct declared variable as it was declared as below

record_id = "R-004"

print(record_id)

# The output is: R-004. this is a string