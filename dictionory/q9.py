# Group Servers by Region
# servers = [
#     {"name": "app01", "region": "us-east"},
#     {"name": "db01", "region": "us-west"},
#     {"name": "app02", "region": "us-east"},
# ]
# Use a dictionary to group server names by region.
# output====>{'us-east': ['app01', 'app02'], 'us-west': ['db01']}
servers = [
    {"name": "app01", "region": "us-east"},
    {"name": "db01", "region": "us-west"},
    {"name": "app02", "region": "us-east"},
]
dic={}
for i in servers:
    region=i["region"]
    name=i["name"]
    if region not in dic:
        dic[region]=[]
    dic[region].append(name)

print(dic)



