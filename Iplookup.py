import requests
print("ip lookup a simple tool designed to give you info on an ip")
print("made by triumphforchaos")
Ipv4 = input('Enter ip here:')

data = requests.get(F'http://ipinfo.io/{Ipv4}/json').json()
print(data)
#made using the ipinfo api
