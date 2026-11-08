"""
RECORD CHECK  -  my version
===========================

Name  :  Julius Paul Lusato
Lane  :  IT     
Date  :  10/3/2026

"""

label = input("Enter the hostname: ")      
first = float(input("GB used: "))     
second = float(input("GB total: "))   

difference = second - first   
percent = (first / second) * 100 
   

print()
print("=" * 34)
print(f"  RECORD CHECK  -  {label}")
print("=" * 34)

print(f"Used: {first:>10.2f}")
print(f"Total: {second:>10.2f}")
print(f"Free: {difference:>+10.2f}")
print(f"Percent: {percent:>7.2f}%")


print("=" * 34)
