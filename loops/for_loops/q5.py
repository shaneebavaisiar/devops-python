# Loop through IPs and filter those in the 192 range
ips = ["10.0.0.1", "192.168.1.1", "172.16.0.5"]

li=[i for i in ips if i.startswith("192.")]
print(li)

