# Check Missing Keys in Config,Find which keys are missing in the config.
# Given:
required_keys = ["host", "port", "user", "password"]
config = {"host": "localhost", "user": "admin"}

for i  in required_keys:
    if i not in config:
        print(i)

