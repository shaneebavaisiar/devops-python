# Find Services Listening on Port > 1024
# services = {"nginx": 80, "ssh": 22, "custom-app": 8080}
# Print services that listen on ports greater than 1024.

services = {"nginx": 80, "ssh": 22, "custom-app": 8080}

for key,value in services.items():
    if value>1024:
        print(f"listening greater than : {key}")