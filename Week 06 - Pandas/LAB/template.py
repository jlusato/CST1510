"""
RECORD CHECK  -  my version
===========================

Name  :  Julius Paul Lusato
Lane  :  IT     
Date  :  11/6/2026 (mm/dd/yyyy)

Run it:   python template.py

"""

import pandas as pd

df = pd.read_csv("records_template.csv")   

df["percent"] = (df["gb_used"] / df["gb_total"]) * 100

df["status"] = df["percent"].apply(
    lambda p: "OVER LIMIT" if p >= 100 else "WARNING" if p >= 90 else "OK"
)

print("All records:")
print(df)

condition = df[df["status"] != "OK"]

print("Need more Attention: ")
print(condition)

