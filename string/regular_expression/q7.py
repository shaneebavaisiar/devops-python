# From a log file, extract only lines with ERROR followed by a 3-digit code: "ERROR 404: Not found" → match
# "ERROR 50: Internal error" → don’t match
import re

lis=[ "ERROR 404: Not found" ,"ERROR 50: Internal error"]
pattern=r"ERROR\s\d{3}"
for i in lis:
    if re.match(pattern,i):
        print(i)