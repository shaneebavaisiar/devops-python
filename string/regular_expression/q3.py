# Get all IP addresses from this text:
import re

txt = "Pinged 10.0.0.1, 172.16.0.10 and 192.168.1.1"
pattern=r"\d+\.\d+\.\d+\.\d+"
print(re.findall(pattern,txt))
