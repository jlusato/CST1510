"""
RECORD CHECK  -  my version
===========================

Name  :  Julius Paul Lusato
Lane  :  IT
Date  :

"""

def check_record(value, limit):
    """Returns difference and percent based on the variables "value" and "limit" and giving them a status """
    difference = limit - value
    percent = (value / limit) * 100

    if percent >=100:
        status = "OVER LIMIT"
    elif percent >= 90:
     status = "wARNING" 
    else:
     status = "OK"

    return difference, percent, status ; 

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

records = [
    {"label": "srv-01", "value": 115.0, "limit": 120.0},
    {"label": "srv-02", "value": 45.0, "limit": 100.0},
    {"label": "srv-03", "value": 130.0, "limit": 120.0},
]

over_limit_count = 0 

for record in records:
    difference, percent, status = check_record(record["value"], record["limit"])
    print_report(record["label"], record["value"], record["limit"], difference, percent, status)


    if status == "OVER LIMIT":
       over_limit_count += 1

print(f"Records over limit: {over_limit_count}")

