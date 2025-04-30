# Parse a Config File
# Convert this string into a dictionary:

txt="host=127.0.0.1;port=3306;user=admin;password=secret"
d=txt.split(";")
print(d)
dic={}
for i in d:
    k=i.split("=")
    dic[k[0]]=k[1]
print(dic)

# or
config_str = "host=127.0.0.1;port=3306;user=admin;password=secret"

config_dict = dict(item.split("=") for item in config_str.split(";"))

print(config_dict)

