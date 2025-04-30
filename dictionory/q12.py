# Invert a Role Dictionary
# roles = {"alice": "admin", "bob": "dev", "carol": "admin"}
# Create a dictionary that maps roles to a list of users.
roles = {"alice": "admin", "bob": "dev", "carol": "admin","shaneeba":"devops","reign":"devops"}
dic={}
for i in roles:
    if roles[i] not in dic:
        dic[roles[i]]=[]
    dic[roles[i]].append(i)

print(dic)