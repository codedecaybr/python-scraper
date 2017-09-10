import requests

## URLS DE BASE ##
URL = "https://www.indeed.com.br/empregos?q=programador&l=S%C3%A3o+Paulo%2C+SP&start=##START_INDEX##"

def obterPagPesquisa(i):
    """
    Recebe um indice de página i, monta a URL adequada,
    baixa o conteúdo e devolve um objeto requests
    com a resposta do servidor HTTP
    """

    # monta a URL:
    rURL = URL.replace("##START_INDEX##", str(i*10) )
    print("Baixando página de pesquisa: " + rURL)
    # download da página de pesquisa:
    searchPage = requests.get(rURL)

    return searchPage

def main():

    # número de páginas de pesquisa a serem baixadas:
    for i in range(1):

        # obtém página de resultado de pesquisa:
        searchPage = obterPagPesquisa(i)

        print(searchPage.text)

main()
