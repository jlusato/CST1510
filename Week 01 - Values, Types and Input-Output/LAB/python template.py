name = "Julius Paul Lusato"
lane = "IT"
date = "10/3/2026"
print(f"Name: {name}")
print(f"Lane: {lane}")
print(f"Date: {date}")

print()
print("=" * 34)
print("RECORD CHECK", "-", lane)
print("=" * 34)

label = str(input("Are you a CS student?(y/n): "))
first = float(input("What year are you in? : "))
second = float(input("What is the value of pi? : "))

difference = second - first
percent = (second / first) * 100

difference = print(f"Difference: {difference:>+5.2f}")
percent = print(f"Percent: {percent:>+10.2f}%") 

print("=" * 34)
