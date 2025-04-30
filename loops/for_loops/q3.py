# Loop through a list of server names and print SSH command for each
servers = ["server1", "server2", "server3"]
for i in servers:
    st=f"ssh user@{i}"
    print(st)