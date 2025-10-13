log_info = [
    "INFO: Operation success ",
    "ERROR: File not found " ,
    "DEBUG: connection" ,
    "ERROR: Database connection failed"
]
for i in log_info :
    if "ERROR" in i:
        print(i)