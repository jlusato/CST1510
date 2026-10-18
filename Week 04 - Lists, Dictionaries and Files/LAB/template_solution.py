def divider():
    print("=" * 34)
    
def status_of(percent):
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"

def check_record(value, limit):
    difference = value - limit
    percent = (value / limit) * 100
    status = status_of(percent)
    return difference, percent, status

def print_report(label, value, limit, status): 
    divider()
    print(f"  RECORD CHECK  -  {label}")
    divider()
    print(f"  {'Used':<14}: {value:g}")
    print(f"  {'Total':<14}: {limit:g}")
    print(f"  {'Status':<14}: {status}")
    divider()

records = [
    {"label": "srv-01", "value": 115.0, "limit": 120.0},
    {"label": "srv-02", "value": 45.0, "limit": 100.0},
    {"label": "srv-03", "value": 130.0, "limit": 120.0},
]

for x in records:
    difference, percent, status = check_record(x["value"], x["limit"])
    print_report(x["label"], x["value"], x["limit"], status)