"""print name and age with fstrings and commas
name = "Julius"
age = 23
print(f"My name is {name},", f"I am {age} years old")
print("My name is", name + ",", "I am", age, "years old")"""


# 1. Print:  The alert said "disk full" on server 'srv-01'
# print('The alert said "disk full"', "on server 'srv-01'")
#print(0.3+1.5)

print("RECORD CHECK ", "-", " my version")
print("=" * 27)

name = "Julius Paul Lusato"
lane = "IT"
date = "10/3/2026"
print("Name ", ":", name)
print("Lane ", ":", lane)
print("Date ", ":", date)

print("=" * 10, "INPUT", "=" * 10)

label = str(input("Enter your Student ID: "))
first = float(input("Coursework1 score: "))
second = float(input("Coursework2 score: "))

print("=" * 10, "PROCESS", "=" * 10)

difference = second - first
percent = (second / first) * 100
print(f"Difference: , {difference:>+10.2f}") 
print(f"Percentage: , {percent:>+10.2f}") 
# or 
#print(f"{percent:.1f} %") 
# to round the percent to 1 decimal place

print("=" * 10, "OUTPUT", "=" * 10)

print()
print("=" * 34)
print(f"RECORD CHECK - {label}")
print("=" * 34)

print(f"Difference: , {difference:>+10.2f}") 
print(f"Percentage: , {percent:>+10.2f}%")

print("=" * 34)

