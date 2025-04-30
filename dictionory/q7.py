# Log Count by Level
# Given a list of logs:
# logs = ["INFO", "ERROR", "INFO", "DEBUG", "ERROR", "INFO"]
# Count how many times each log level appears using a dictionary.
logs = ["INFO", "ERROR", "INFO", "DEBUG", "ERROR", "INFO"]
dic={}
for i in logs:
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1

print(dic)


