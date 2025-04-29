# Check if a line starts with ERROR:
import re

l = ["ERROR: Disk is full",
     "WARNING: CPU high"]
for i in l:
 if re.match(r"^ERROR",i):
   print("MATCHED :",i)
 else:
   print("NOT MATCHED :",i)


