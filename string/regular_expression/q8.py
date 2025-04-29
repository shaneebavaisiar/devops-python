# Get all .conf files from this list:
import re

l=["nginx.conf", "hosts", "sshd_config", "my.conf"]
pattern=r"\w\.conf"
for i in l:
    if re.findall(pattern,i):
        print(i)

li=[i for i in l if i.endswith(".conf")]
print(li)