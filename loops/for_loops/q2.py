# Print only lines that start with ERROR
import re

logs = ["INFO: Started", "ERROR: Disk full", "WARNING: High memory usage"]
pattern=r"ERROR"
for i in logs:
    if re.match(pattern,i):
        print(i)
