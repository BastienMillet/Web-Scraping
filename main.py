from random import random, uniform
import requests
from bs4 import BeautifulSoup
import time

url = 'https://www.siteweb.com'
result = requests.get(url)

if result.ok:
    listHrefDepartement = []
    listDepartement = []
    listHrefVille = []
    listNomVille = []
    listClassement = []
    validation = "Ville,Classement\n"
    f = open("test.txt", "a")
    f.write(validation)
    f.close()
    validation = ""
    soup = BeautifulSoup(result.text, features="html.parser")
    
    divs = soup.findAll('div', {'class' : 'flex-three d-flex flex-column justify-content-center align-items-center align-items-lg-start live-in-list'})
    
    for div in divs:
        
        balisesA = div.findAll('a')
        for b in balisesA:
            hrefBaliseA = b['href']
            listHrefDepartement.append(hrefBaliseA)
    
    for varlistHrefDepartement in listHrefDepartement:
        departement = varlistHrefDepartement.replace("/vivre-dans-le-", "")
        urlDepartement = 'https://www.siteweb.com' + varlistHrefDepartement

        result = requests.get(urlDepartement)

        if result.ok:

            soup = BeautifulSoup(result.text, features = "html.parser")
            lis = soup.findAll('li', {'class' : 'city-item'})

            for li in lis:
                try:
                    baliseA = li.find('a')
                    baliseAtext = baliseA.text
                    baliseAtext = baliseAtext.replace(" ", "")
                    baliseAtext = baliseAtext.replace("\n", "")
                    hrefBaliseA = baliseA['href']
                    listNomVille.append(baliseAtext)
                    listHrefVille.append(hrefBaliseA)
                except Exception as e:
                    baliseA = None
            j = 1
            for varlistHrefVille in listHrefVille:    
                urlVille = 'https://www.siteweb.com' + varlistHrefVille
                result = requests.get(urlVille)

                if result.ok:
                   
                    soup = BeautifulSoup(result.text, features = "html.parser")
                    divs = soup.findAll('div', {'class' : 'ranking-card'})
                    resultat = divs[0].find('p', {'class' : 'font-weight-bold'}).text
                    a = ""
                    for i in range(0, len(resultat)):
                        if resultat[i].isdigit() == True:
                            a = a + resultat[i]
                        else:
                            break
                    listClassement.append(a)
                    print(j)
                    j = j + 1
                    time.sleep(1)
                    
        
    for i in range(0, len(listClassement)):
        validation = validation + listNomVille[i] + ',' + listClassement[i] + '\n'
        f = open("test.txt", "a")
        f.write(validation)
        f.close()
        validation = ""


    

    
       