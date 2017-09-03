import requests
from bs4 import BeautifulSoup
from auxiliar import Requisito


## URLS DE BASE ##
URL = "https://www.indeed.com.br/empregos?q=programador&l=S%C3%A3o+Paulo%2C+SP&start=##START_INDEX##"
baseURL = "https://www.indeed.com.br"

lReqs = ["Java", "PHP", "Net", "C++", "Pyhon", " C ", "C#", " R ", "VBA",
    "Excel", "Ruby", "Android", "CSS", "HTML", "Swift"]


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

def obterPagVaga(jobLink):
    """
    Recebe um objeto do BeautifulSoup com o link extraído
    para um anúncio de vaga no Ideed e devolve o objeto
    do BeautifulSoup representando os detalhes da vaga
    anunciada.
    """

    print("\tBaixando página da vaga: " + jobLink.get("title"))
    # download da página da vaga:
    with requests.Session() as s:
        s.max_redirects = 1
        try:
            jobPage = s.get(baseURL + jobLink.get("href"), timeout=2)
        except requests.exceptions.TooManyRedirects:
            print("\t\tToo many redirects. Maybe it is a sponsored job.")
            return None
    # verifica se a página baixada pertence
    # ao domínio do indeed.
    # as vagas patrocinadas redirecionam para sites
    # externos, com estruturas desconhecidas
    if "indeed.com.br" not in jobPage.url:
        print("\t\tSponsored job. Skipping.")
        return None
    # conversão para o objeto do BeautifulSoup:
    jobSoup = BeautifulSoup(jobPage.text, 'html.parser')

    return jobSoup

def procuraSalario(jobSoup):
    """
    Navega na página de detalhe da vaga buscando pelo salário
    anunciado. Devolve um vetor com o parágrafo de ocorrência.
    """
    salarioVetor = []
    # procura o salário no campo mais comum:
    campoSalario = jobSoup.find("span", attrs={"style":"white-space: nowrap"})
    # se encontra, picota o parágrafo e armazena no vetor:
    if campoSalario is not None:
        salarioVetor = campoSalario.get_text().split(" ")
    # se não encontra, faz a busca no corpo da vaga:
    else:
        campoSalario = jobSoup.find("span", id="job_summary")
        if campoSalario is not None:
            # separa os paragráfos e navega por cada um:
            paragraphs = campoSalario.find_all("p")
            for p in paragraphs:
                # procura pela palavra Salário
                if "Salário: " in p.get_text():
                    # picota o parágrafo e armazena no vetor:
                    salarioVetor = p.get_text().split(" ")
    return salarioVetor

def converteSalario(salarioVetor):
    """
    Converte um parágrafo com a ocorrência de salário em
    um número decimal.
    Ex:
        paragrafo <= 'Salário: de R$ 1.800 - R$ 2.000'
        vetor <= ['Salário:', 'de', 'R$', '1.800', '-', 'R$', '2.000']
        retorno <= ( 1800.00 + 2000.00 ) / 2
    """
    # para cada palavra dentro do vetor:
    f = 0
    cont = 0
    for s in salarioVetor:
        # tenta fazer a conversao para float:
        try:
            f += 1000*float(s)
        # caso a palavra não seja uma representação válida de float:
        except ValueError:
            # passa para a próxima
            continue
        cont += 1
    if cont != 0:
        f = f/cont
    return f

def procuraRequisitos(jobSoup, requisitos, salario):
    descricao = jobSoup.find("span", id="job_summary")
    if descricao is not None:
        # separa os paragráfos e navega por cada um:
        conteudoDescricao = descricao.get_text().lower()
        for req in requisitos:
            if req.lower() in conteudoDescricao:
                print("\t\t" + req)
                requisitos[req].add(salario)
                continue

def inicializaRequisitos(listaRequisitos):
    reqsDct = {}
    for r in listaRequisitos:
        reqsDct[r] = Requisito(r)
    return reqsDct

def main():

    contVagas = 0
    somaSalario = 0

    requisitos = inicializaRequisitos(lReqs)

    # número de páginas de pesquisa a serem baixadas:
    for i in range(0,1):

        # obtém página de resultado de pesquisa:
        # obtém página de resultado de pesquisa:
        searchSoup = obterPagPesquisa(i)
        # encontra todos os links de anúncios de vagas
        jobsLinks = searchSoup.find_all(class_="turnstileLink")

        # para cada link encontrado...
        for jobLink in jobsLinks:
            # verifica se é válido (pula links com nomes de empresas)
            if jobLink.get("title") is None:
                continue

            # baixa a página com o detalhe da vaga:
            jobSoup = obterPagVaga(jobLink)
            if jobSoup is None:
                continue

            # procura a informação de salário dentro do detalhe da vaga:
            salarioVetor = procuraSalario(jobSoup)
            # tenta converter o salário encontrado para um número decimal:
            salario = converteSalario(salarioVetor)
            if salario != 0:
                print("\t\tR$ %.2f" %(salario))
                somaSalario += salario
                contVagas += 1
            procuraRequisitos(jobSoup, requisitos, salario)

        input()

    print("Vagas com Salário Encontradas: %d" %(contVagas))
    print("Média das Ofertas: R$ %.2f" %(somaSalario/contVagas))

    for req in requisitos:
        requisitos[req].printEstat()

main()
