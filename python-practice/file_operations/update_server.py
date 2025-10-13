def update_server_config(file_path,key,value):
    with open(file_path,"r") as file:
        lines= file.readlines()
    with open(file_path,"w") as file1:
        for line in lines:
            if key in line:
                file1.write(key + "=" + value + "\n")
            else:
                file1.write(line)
update_server_config("/Users/alekhyabheemarasetty/Desktop/python-practice/file_operations/server.conf","MAX_CONNECTIONS","1000")                        

