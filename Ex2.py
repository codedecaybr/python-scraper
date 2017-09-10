import requests
from bs4 import BeautifulSoup


## URLS DE BASE ##
URL = "https://www.indeed.com.br/empregos?q=programador&l=S%C3%A3o+Paulo%2C+SP&start=##START_INDEX##"

def obterPagPesquisa(i):
    """
    Recebe um indice de página i, monta a URL adequada,
    baixa o conteúdo e devolve um objeto do BeautifulSoup
    representando o conteúdo da página de pesquisa do Indeed.
    """

    # monta a URL:
    rURL = URL.replace("##START_INDEX##", str(i*10) )
    print("Baixando página de pesquisa: " + rURL)
    # download da página de pesquisa:
    searchPage = requests.get(rURL)
    # conversão para o objeto do BeautifulSoup:
    searchSoup = BeautifulSoup(searchPage.text, 'html.parser')

    return searchSoup

def main():

    # número de páginas de pesquisa a serem baixadas:
    for i in range(1):

        # obtém página de resultado de pesquisa:
        # obtém página de resultado de pesquisa:
        searchSoup = obterPagPesquisa(i)
        # encontra todos os links de anúncios de vagas
        jobsLinks = searchSoup.find_all(class_="turnstileLink")

        # para cada link encontrado...
        for jobLink in jobsLinks:
            print(jobLink.get("href"))


main()
