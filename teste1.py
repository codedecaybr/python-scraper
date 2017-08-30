import requests
from bs4 import BeautifulSoup
import re

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
        if "indeed.com.br" not in jobPage.url:
            print("\t\tSponsored job. Skipping.")
            continue
        jobSoup = BeautifulSoup(jobPage.text, 'html.parser')
        ps = jobSoup.find_all("span", attrs={"style":"white-space: nowrap"})
        for p in ps:
            print("\t\t" + p.get_text())

        ps = jobSoup.find("span", id="job_summary")
        if ps is not None:
            ps = ps.find_all("p")
            for p in ps:
                if "Salário: " in p.get_text():
                    print("\t\t" + p.get_text())

    print()
