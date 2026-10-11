def divider():
    print("=" * 34)
    
def status_of(percent):
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"

name = input("Hostname: ")
used = float(input("GB used: "))
total = float(input("GB total: "))

difference = used - total
percent = (used / total) * 100
status = status_of(percent)

divider()
print(f"  RECORD CHECK  -  {name}")
divider()
print(f"  {'Used':<14}: {used:g}")
print(f"  {'Total':<14}: {total:g}")
print(f"  {'Status':<14}: {status}")
divider()