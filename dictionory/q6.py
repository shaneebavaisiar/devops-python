# Update Configurations
# You have:
# config = {"port": 80, "debug": False}
# Update the port to 8080 and set debug to True.
config = {"port": 80, "debug": False}
for i in config:
    if i=="port":
        config[i]=8080
    elif i=="debug":
        config[i]=True
print(config)


