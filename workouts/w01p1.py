record_id = input("Record ID : ")
value     = float(input("Value     : "))
limit     = float(input("Limit     : "))

# ------------------------------------------------------------------ STORE
# Week 4. For now, one record lives in three variables.

# ---------------------------------------------------------------- PROCESS
difference = value - limit
percent    = (value / limit) * 100

status = "OVER LIMIT" if difference > 0 else "OK"   # <- Week 2

# ----------------------------------------------------------------- OUTPUT
print()
print("=" * 34)
print(f"  RECORD CHECK  -  {record_id}")
print("=" * 34)
print(f"  Value       : {value:>10.2f}")
print(f"  Limit       : {limit:>10.2f}")
print(f"  Difference  : {difference:>+10.2f}")
print(f"  Of limit    : {percent:>9.1f} %")
print(f"  Status      : {status:>10}")
print("=" * 34)