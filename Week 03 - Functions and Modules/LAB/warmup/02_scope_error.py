# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.

def check(value, limit):
    """Returns the status after comparing the two parameters"""
    status = "OVER LIMIT" if value > limit else "OK"
    return status

status = check(87, 100)

print(status)
