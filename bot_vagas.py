s = "http://oportunidades.pucsp.br/ingresar"
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
from urllib.request import urlopen
import time

driver = webdriver.Chrome("C:\\Users\\sabri\\Desktop\\chromedriver.exe") #abre o chrome
driver2 = webdriver.Chrome("C:\\Users\\sabri\\Desktop\\chromedriver.exe") #abre o chrome
driver.get(s)
input("digite qualquer coisa após logar e tecle enter")



def enderecos():
    fonte = driver2.page_source #página onde procura os links
    bsObj = BeautifulSoup(fonte, "html.parser") # o que é para o bfs ler, processar o html
    a = bsObj.find_all("h2",{"class":"elcargo"})
    for t in a:
        try:
            if Analisador(t.a.get("href")): # constar economia, printa o link
                candidatura(t.a.get("href"))
            else:
                next
        except:
            next
def Analisador(end):
    analisarTexto = end
    html = urlopen(analisarTexto) #baixa o html do site
    bsObj = BeautifulSoup(html, "html.parser")
    #Carreira
    variavel = []
    for i in bsObj.find_all("ul",{"class": "oferta_lista"})[0].find_all("li"):
        variavel.append(i.text)
    x = "".join(variavel) #'Carreira'
    validacao = ['economia', 'economicas', 'econômicas'] #validação carreira
    qtd = [i for i in validacao if i in x.lower()]

    if len(qtd)>0:
        return True
    else:
        return False

def candidatura(end):
    try:
        driver.get(end)
        blue = driver.find_element_by_class_name("blue_btn")
        blue.click()
    except:
        _=""


driver2.get("http://oportunidades.pucsp.br/vagas-trabalho-emprego/region-Sao-Paulo/")
#time.sleep(10)
enderecos()

for i in range(1,17):
    try:
        driver2.find_element_by_id("nextPageEmpresa").click()

        enderecos()
    except:
        next
        



