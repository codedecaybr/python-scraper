import requests
from bs4 import BeautifulSoup
n = 1503614732084
URL = "https://www.indeed.com.br/empregos?q=programador&l=S%C3%A3o+Paulo%2C+SP&start=##START_INDEX##"
links = []
for i in range(1,4):
    rURL = URL.replace("##START_INDEX##", str(i*10) )
    print(rURL)
    page = requests.get(rURL)
    soup = BeautifulSoup(page.text, 'html.parser')
    res = soup.find_all(class_="turnstileLink")
    for i in range(len(res)):
        link = res[i].get("href")
        print(link, end="")
        if link in links:
            print(" REPETIDO")
        else:
            print(" NOVO")
            links.append(link)
    input()
