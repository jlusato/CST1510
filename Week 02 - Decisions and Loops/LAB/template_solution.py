label = input("Label: ")
value = float(input("Value: "))
limit = float(input("Limit: "))

difference = limit - value
percent = (value / limit) * 100


if percent >= 100:
    status  = "OVER LIMIT"
elif percent >= 90:
    status = "WARNING"
else:
    status = "OK"

print()
print("=" * 34)
print(f"  RECORD CHECK  -  {label}")
print("=" * 34)

print(f"{'Used':<10}: {value:>10.2f}")
print(f"{'Total':<10}: {limit:>10.2f}")
print(f"{'Free':<10}: {difference:>10.2f}")
print(f"{'Percent':<10}: {percent:>10.2f}%")
print(f"{'Status':<10}: {status:>10}")

print("=" * 34)
