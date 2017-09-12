import requests
from bs4 import BeautifulSoup

# uso simples do get
URL = "https://www.indeed.com.br/empregos?q=programador&l=S%C3%A3o+Paulo%2C+SP&start=20"
response = requests.get(URL)
print(respose.text)

soup = BeautifulSoup(response.txt, "html.parser")
soup.title
soup.title.get_text()
