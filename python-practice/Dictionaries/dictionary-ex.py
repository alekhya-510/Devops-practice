server_config = {
    'server1': {'ip': '192.168.1.1', 'port': 8080, 'status': 'active'},
    'server2': {'ip':'192.168.38.1','port': 8000 ,'status':'inactive'},
    'server3': {'ip':'192.168.33.1','port': 9000 ,'status':'active'}
}
def get_server_status(server_name):
    return server_config.get(server_name, {}).get('status', 'server not found')

server_name= input()
ser_status= get_server_status(server_name)
print(f"{server_name}: {ser_status}")