"""
RECORD CHECK  -  my version
===========================

Name  :   Julius Paul Lusato
Lane  :   IT      
Date  :   25/10/2026

Run it:   python template.py.
"""

class Record:
    over_limit_count = 0

    def __init__(self, label, value, limit):
        self.label = label
        self.value = value
        self.limit = limit

    def percent(self):
        return (self.value / self.limit) * 100

    def status(self):
        if self.percent() >= 100:
            return "OVER LIMIT"
        elif self.percent() >= 90:
            return "WARNING"
        else:
            return "OK"
        
records = [
    Record("srv-001", 87, 120),
    Record("srv-002", 118, 120),
    Record("srv-003", 150, 120)
]  

for record in records:
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {record.label}")
    print("=" * 34)

    # your report lines go here
    condition = record.status()
    print(f" GB used: {record.value}") 
    print(f" GB total: {record.limit}")
    print(f" Condition: {condition}")

    percent = record.percent()
    status = record.status()
    
    if condition == "OVER LIMIT":
        Record.over_limit_count += 1
            
    print("=" * 34)

print(f"Records over limit: {Record.over_limit_count}")
