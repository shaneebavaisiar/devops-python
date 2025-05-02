def server_update(file_path,key,value):

    with open(file_path) as file:
        content=file.readlines()
        # print(content)
    with open(file_path,"w") as file:
        for line in content:
            if key in line:
                file.write(f"{key}={value}\n")
            else:
                file.write(line)

server_update("server.conf","MAX_CONNECTIONS",10)