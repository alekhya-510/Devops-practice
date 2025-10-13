


server_name= "Hanvika"
port= 80
is_https_enabled= 'true'
max_connections= 1000

print(f"Server_name : {server_name}")
print(f"Port : {port}")
print(f"Is HTTPS enabled: {is_https_enabled}")
print(f"Max connections: {max_connections}")

port= 443
is_https_enabled= 'false'

print(f"Updated Port : {port}")
print(f"Updated HTTPS enabled: {is_https_enabled}")
