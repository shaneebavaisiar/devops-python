import requests

url = "https://api.github.com/repos/kubernetes/kubernetes/pulls"
response = requests.get(url).json()
count = 0
dic = {}
lis = []
for i in response:
    pr_user = i["user"]["login"]
    if pr_user not in dic:
        dic[pr_user] = 1
    else:
        dic[pr_user] += 1
print(dic)
lis = []
for name, pr in dic.items():
    lis.append({"name": name, "pull_req": pr})
print(lis)
