import re
# Extract all numbers from this string:
txt = "Server uptime: 432 days, 15 hours, 22 minutes"

pattern=r"\d+"
lis=re.findall(pattern,txt)
print(lis)
