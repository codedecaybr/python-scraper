import requests
from bs4 import BeautifulSoup
n = 1503614732084
URL = "https://www.indeed.com.br/empregos?q=programador&l=S%C3%A3o+Paulo%2C+SP&start=##START_INDEX##"
baseURL = "https://www.indeed.com.br"
links = []
for i in range(1,4):
    rURL = URL.replace("##START_INDEX##", str(i*10) )
    print("Baixando página de pesquisa: " + rURL)
    page = requests.get(rURL)
    soup = BeautifulSoup(page.text, 'html.parser')
    res = soup.find_all(class_="turnstileLink")
    for i in range(len(res)):
        if res[i].get("title") is None:
            continue
        print("\tBaixando página da vaga: " + res[i].get("title"))
        jobPage = requests.get(baseURL + res[i].get("href"))
        jobSoup = BeautifulSoup(jobPage.text, 'html.parser')
        ps = soup.find_all(class_="p")
        for p in ps:
            if "Salário" in p:
                print (p.get_text())
    input()
