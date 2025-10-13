import requests
url= f"https://api.github.com/repos/kubernetes/kubernetes/pulls"
response= requests.get(url)
#print(response.json())
complete_detail = response.json()
for i in range(len(complete_detail)):
    print(complete_detail[1]["user"]["login"])