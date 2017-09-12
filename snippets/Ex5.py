import requests
from bs4 import BeautifulSoup

# uso simples do get PARA VAGA DE EMPREGO
URL = "https://www.indeed.com.br/cmp/TPA-SA%C3%9ADE/jobs/Web-Designer-Programador-46a40394f66aecc9?q=programador"
response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")
descricao = soup.find("span", id="job_summary")
print(descricao)
print(descricao.get_text())
print(descricao.get_text().lower())
