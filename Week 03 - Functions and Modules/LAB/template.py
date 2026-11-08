"""
RECORD CHECK  -  my version
===========================

Name  :  Julius Paul Lusato
Lane  :  IT     
Date  :

"""

def status_of(percent):
    """Returns "OVERLIMIT", "WARNING" OR "OK" based on the variable "percent" """
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"

def check(value, limit):
    """Returns difference and percent based on the variables "value" and "limit" """
    difference = limit - value
    percent = (value / limit) * 100
    return difference, percent ; 

def print_report(label, value, limit, difference, percent, status):
    """Prints the report check record for one record"""

    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {label}")
    print("=" * 34)

    print(f"  {'Used':<14}: {value:>10.2f}")
    print(f"  {'Total':<14}: {limit:>10.2f}")
    print(f"  {'Free':<14}: {difference:>10.2f}")
    print(f"  {'Percent':<14}: {percent:>9.2f}%")
    print(f"  {'Status':<14}: {status:>10}")

    print("=" * 34)


over_limit = 0

while True:
    label = input("Hostname (OR 'quit' to stop): ")
    if label == "quit":
        break

    value = float(input("Enter a value: "))
    limit = float(input("Enter the limit: "))

    difference, percent = check(value, limit)
    status = status_of(percent)

    print_report(label, value, limit, difference, percent, status)

    if status == "OVER LIMIT":
        over_limit += 1

print(f"Records over limit: {over_limit}")

