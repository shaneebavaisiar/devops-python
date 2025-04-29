import re

name = "shaneeba"
# upper
print(name[0].upper() + name[1:])
# lower
a = "REIGN"
print(a.lower())
# len
print(len(a))
# strip
b = "        cat dog/lion        "
c = "////cat talk/////"
print(b.strip())
print(c.strip("/"))
# split
word = "my name is shaneeba:and i am a student/i have a baby boy:my place is perinthelmanna"
print(word.split(":"))
# concatenate
first_name = "shaneeba"
last_name = "vaisiar"
print(first_name + " " + last_name)

# substring (find()/in)
txt = "i am shaneeba "
substring = "am"
if substring in txt:
    print(substring, "found in text")
# repalce

t = "my name is shaneeba"
k = t.replace("shaneeba", "reign")
print(k)

# join
l = ["cat", "dog", "lion", "elephant"]
join_string = " ".join(l)
join_s = "\n".join(l)
print(join_string)
print(join_s)

# startswith and endswith
log = "ERROR: Disk full"
if log.startswith("ERROR"):
    print("error found")
file = "backup.tar.gz"
if file.endswith(".gz"):
    print("this is a compressed file")

log_lines = [
    "INFO: System started",
    "WARNING: Low memory",
    "ERROR: Disk full"
]
for i in log_lines:
    if i.startswith("WARNING"):
        print("this file contains warning log")

files = ["nginx.conf", "dockerfile", "readme.md"]
for i in files:
    if i.endswith(".conf"):
        print("config file :",i)

# string formating

my="shaneeba"
print(f"my name is {my}")

# regex
