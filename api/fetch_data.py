import requests
url = "https://declarator.org/api/v1/search/person-sections/?name=Антов"
response = requests.get(url)

print(response.json())