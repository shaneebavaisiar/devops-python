# Loop through a list of ports and print if port is open
ports = [22, 80, 443, 8080]
for i in ports:
    open=f"port {i} is open"
    print(open)