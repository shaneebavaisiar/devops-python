# Keep checking CPU usage until it's below 80%
# (Simulate with a list of values)

cpu_usages = [90, 85, 78, 60]
index=0
while index<len(cpu_usages) and cpu_usages[index]>=80:
    print(f"cpu usage is high :{cpu_usages[index]}%")
    index += 1

if index<len(cpu_usages):
    print(f"cpu usage is normal :{cpu_usages[index]}%")


