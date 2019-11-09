from functions import *
path_file = 'WorldCups.csv'
url_api = 'https://raw.githubusercontent.com/lsv/fifa-worldcup-2018/master/data.json'
url_asist = 'https://en.wikipedia.org/wiki/2018_FIFA_World_Cup'
url_wm = 'https://www.britannica.com/sports/World-Cup-football'
url_gtq ='https://www.footballhistory.org/world-cup/index.html'

dataframe(path_file,url_api,url_asist,url_wm,url_gtq)

'''
df = loadfile(path_file) #cargo el archivo
results = loadsoup(url_api) #cargo la url de la api
Rusia = rusia(results) #creo la fila de Rusia (sin la asistencia)

Rusia['Attendance'] = asis(url_asist) #obtiene la asistencia de Rusia
dfr  = df.append(Rusia, ignore_index=True) #agrego la fila de Rusia

dfr['FinGamWinMode'] = modwm(url_wm) #agrego la columna de modalidad de juego

dfr['GamesQual'] = gtq(url_gtq)
'''
