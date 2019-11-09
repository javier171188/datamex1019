import json
import requests
import pandas as pd
import re
from bs4 import BeautifulSoup as bs

def dataframe(path_file,url_api,url_asist,url_wm,url_gtq):
    df = loadfile(path_file) #cargo el archivo
    results = loadsoup(url_api) #cargo la url de la api
    Rusia = rusia(results) #creo la fila de Rusia (sin la asistencia)

    Rusia['Attendance'] = asis(url_asist) #obtiene la asistencia de Rusia

    dfr  = df.append(Rusia, ignore_index=True) #agrego la fila de Rusia
    dfr['Attendance'] = dfr['Attendance'].apply(clean_asis) #Ahora se limpia toda la columna 
    dfr['FinGamWinMode'] = modwm(url_wm) #agrego la columna de modalidad de juego

    dfr['GamesQual'] = gtq(url_gtq) #agrego columna # de juegos para calificar

    dfr.to_csv('updatedWQ.csv', index=False)
    print(dfr)


def loadfile(path):
    df = pd.read_csv (path)
    return df

def loadsoup(url):
    response = requests.get(url)
    results = response.json()
    return results

def rusia(results):
    Rusia = {'Country':'Russia'}
    Rusia['QualifiedTeams'] = results['teams'][-1]['id']
    Rusia['Winnerid'] = results['knockout']['round_2']['matches'][0]['winner']
    Rusia['Year'] = results['knockout']['round_2']['matches'][0]['date'][0:4]

    for e in results['teams']:#esto se puede hacer una funcion
        if e['id']==Rusia['Winnerid']:
            Rusia['Winner'] = e['name']
    Rusia.pop("Winnerid")

    if results['knockout']['round_2']['matches'][0]['home_team'] != results['knockout']['round_2']['matches'][0]['winner']:
        Rusia['Runners-Upid'] = results['knockout']['round_2']['matches'][0]['home_team']
    else:
        Rusia['Runners-Upid'] = results['knockout']['round_2']['matches'][0]['away_team']

    for e in results['teams']:
        if e['id']==Rusia['Runners-Upid']:
            Rusia['Runners-Up'] = e['name']
    Rusia.pop("Runners-Upid")

    Rusia['Thirdid'] = results['knockout']['round_2_loser']['matches'][0]['winner']

    for e in results['teams']:
        if e['id']==Rusia['Thirdid']:
            Rusia['Third'] = e['name']
    Rusia.pop("Thirdid")


    if results['knockout']['round_2_loser']['matches'][0]['winner'] != results['knockout']['round_2_loser']['matches'][0]['home_team']:
        Rusia['Fourthid'] = results['knockout']['round_2_loser']['matches'][0]['home_team']
    else:
        Rusia['Fourthid'] = results['knockout']['round_2_loser']['matches'][0]['away_team']

    for e in results['teams']:
        if e['id']==Rusia['Fourthid']:
            Rusia['Fourth'] = e['name']
    Rusia.pop("Fourthid")

    goals =0

    for e in results['groups']:
        for f in range(len(results['groups'][e]['matches'])):
            goals = goals + results['groups'][e]['matches'][f]['home_result']
            goals = goals + results['groups'][e]['matches'][f]['away_result']

    for e in results['knockout']:
        #print(results['knockout'][e]['matches'])
        for i in range(len(results['knockout'][e]['matches'])):
            #print(results['knockout'][e]['matches'][i]['home_result'])
            #print(results['knockout'][e]['matches'][i]['away_result'])
            goals = goals + results['knockout'][e]['matches'][i]['home_result']
            goals = goals + results['knockout'][e]['matches'][i]['away_result']
    Rusia['GoalsScored'] = goals

    Rusia['MatchesPlayed']=results['knockout']['round_2']['matches'][0]['name']

    return Rusia

def asis(url_asist):
     response = requests.get('https://en.wikipedia.org/wiki/2018_FIFA_World_Cup')
     #print(response)
     asis = response.content
     soup=bs(asis, 'html.parser')
     table=soup.find_all('tbody')
     look =table[0].find_all('td')

     lstlook= []
     for e in look:
        t = re.findall('per match',str(e))
        if t != []:
            lstlook.append(e)

     leni= max([len(e.text) for e in lstlook])
     for e in lstlook:
        if len(e.text) == leni:
            asinc = e.text


     asi = asinc.split('\xa0')[0]
     return asi.replace(',','')


def clean_asis(s):
    s = str(s).replace('.','')
    return int(s)



def modwm(url_wm):
    response = requests.get('https://www.britannica.com/sports/World-Cup-football')
    #print(response)
    winm = response.content
    soup=bs(winm, 'html.parser')
    table=soup.find_all('tbody')
    elements = table[0].find_all('td')
    #print(elements)


    c = 0
    winmod = []
    for i in range(len(elements)):
        if c == 1:
            t = re.findall('\*', elements[i].text)
            if len(t) == 2:
                winmod.append('Penalty kicks')
            elif len(t) == 1:
                winmod.append('Extra time')
            else:
                winmod.append('Regular time')
            c=0
        t = re.findall('\d{4}', elements[i].text)
        if  t!=[]:
            c=1
    #print(winmod)

    return winmod


def gtq(url_gtq):

    response = requests.get(url_gtq)
    #print(response)
    cit = response.content

    soup=bs(cit, 'html.parser')
    table = soup.find_all('table')

    qual = []
    for i in range(1,len(table[-1].find_all('tr'))):
        #print(str(table[-1].find_all('tr')[i]).split('<td class="left">')[1].split('</td>')[2].replace('<td>',''))
        qual.append(str(table[-1].find_all('tr')[i]).split('<td class="left">')[1].split('</td>')[2].replace('<td>',''))
    for i in range(len(qual)):
        qual[i] = qual[i].replace('\n','')
        if 'no' in  qual[i]:
            qual[i] = 0
        qual[i] = int(qual[i])

    return qual
