import requests

# uso simples do get
URL = "https://www.indeed.com.br/empregos?q=programador&l=S%C3%A3o+Paulo%2C+SP&start=20"
response = requests.get(URL)
print(response.status_code)
print(respose.text)

# construindo a URL dinâmicamente
i = 30
URL = "https://www.indeed.com.br/empregos?q=programador&l=S%C3%A3o+Paulo%2C+SP&start=##START_INDEX##"
rURL = URL.replace("##START_INDEX##", i)
print(rURL)
response = requests.get(rURL)
print(response.status_code)
print(respose.text)
