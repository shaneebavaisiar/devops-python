# Server Status Map
# You have a dictionary like:
# servers = {"web01": "running", "db01": "stopped", "cache01": "running"}
# Write a program to print only the servers that are stopped.

servers = {"web01": "running", "db01": "stopped", "cache01": "running"}
for server in servers:
    if servers[server]=="stopped":
        print(f"{server} is stopped")