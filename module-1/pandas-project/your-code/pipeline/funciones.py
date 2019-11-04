# importar las bibliotecas necesarias******************************************************************
import pandas as pd
import re


#leer el archivo*************************************************************************************
def leer(arc):
    df = pd.read_csv(arc)
    return df

#Atacamos la columna    type **************************************************************************************+
def type_col(df):
    df.Type.fillna('No information', inplace = True)
    df.Type[df.Type.str.startswith('Bo')]='Boating'
    df.Type[df.Type.str.startswith('Inv')]='No information'
    return df

#Country ***************************************************************************************************
def country_col(df):
    df.Country.fillna('No information', inplace = True)
    df.Country = df.Country.apply(lambda x: str(x).upper())

    def interr(s):
        if '?' in str(s):
            s = 'No information'
            return s
    df.Country = df.Country.apply(interr)

    def amp(s):
        s = str(s).replace('&', 'Y')
        return s
    df.Country = df.Country.apply(amp)

    def spec(s):
        if r'/' in s:
            s = 'NO INFORMATION'
        return s
    df.Country = df.Country.apply(spec)

    def ocean(s):
        if 'OCEAN' in s or 'SEA' in s or 'BETWEEN' in s or 'GULF' in s or 'DIEGO GARCIA' in s:
            s = 'NO INFORMATION'
        elif 'ST. MAARTIN' in s:
            s = 'ST. MAARTIN'
        return s
    df.Country = df.Country.apply(ocean)

    esp_1 = lambda x: re.sub('^\s', "", str(x))
    esp_2 = lambda x: re.sub('\s$', "", str(x))
    df['Country'] = df['Country'].apply(esp_1)
    df['Country'] = df['Country'].apply(esp_2)

    return df

#Sex *********************************************************************************************
def sex_col(df):
    dfc = df.rename(columns = {'Sex ':'Sex'})
    dfc.Sex.fillna('No information', inplace = True)
    def cleans(s):
        if 'N' in str(s) or 'lli' in str(s) or r'.' in str(s):
            s = 'No information'
        return s
    dfc.Sex = dfc.Sex.apply(cleans)

    def male(s):
        if 'M' in str(s):
            s = 'M'
        return s
    dfc.Sex = dfc.Sex.apply(male)


    return dfc


#Fatal ********************************************************************************+**********+
def fatal_col(dfc):
    dfc['Fatal (Y/N)'].fillna('No information', inplace = True)
    def fatal(s):
        if 'UNKNOWN' in str(s):
            s = 'No information'
        elif 'N' in str(s) or 'n' in str(s) or 'F' in str(s):
            s = 'N'
        elif 'Y' in str(s):
            s = 'Y'
        else:
            s = 'No information'

        return s
    dfc['Fatal (Y/N)'] = dfc['Fatal (Y/N)'].apply(fatal)

    return dfc

#Activity *********************************************************************************************
def activity_col(dfc):
    dfc.Activity.fillna('No information', inplace = True)
    def funct(s):
        if 'Surfing' in s or 'surfing' in s:
            s = 'Surfing'
        elif 'Fishing' in s or 'fishing' in s:
            s = 'Fishing'

        return s
    dfc.Activity = dfc.Activity.apply(funct)
    return dfc

#Age ***************************************************************************************************
def age_col(dfc):
    dfc.Age.fillna('No information', inplace = True)
    esp_1 = lambda x: re.sub('^\s', "", str(x))
    esp_2 = lambda x: re.sub('\s$', "", str(x))
    dfc.Age = dfc.Age.apply(esp_1)
    dfc.Age = dfc.Age.apply(esp_2)
    def num_d(s):
        if len(str(s)) > 2:
            return 'No information'
        else:
                return s
    dfc.Age = dfc.Age.apply(num_d)
    def let(s):
        a = re.findall('\D', str(s))
        if len(a) !=0:
            return 'No information'
        else:
            return s
    dfc.Age = dfc.Age.apply(let)
    def noesp(s):
        if ' ' in s or '' == s:
            return 'No information'
        else:
            return int(s)
    dfc.Age = dfc.Age.apply(noesp)

    return dfc


#Species*************************************************************************************************
def species_col(dfc):
    dfs = dfc.rename(columns = {'Species ':'Species'})
    dfs.Species.fillna('no information', inplace = True)
    dfs.Species = dfs.Species.apply(lambda x: str(x).lower())
    def nulsh(s):
        if '?' in str(s) or 'not' in str(s):
            s = 'no information'
        return s
    dfs.Species = dfs.Species.apply(nulsh)
    esp_1 = lambda x: re.sub('^\s', "", str(x))
    esp_2 = lambda x: re.sub('\s$', "", str(x))
    dfs.Species = dfs.Species.apply(esp_1)
    dfs.Species = dfs.Species.apply(esp_2)

    def comsp(s):
        if 'white' in s:
            s = 'white'
        elif 'mako' in s:
                s= 'mako'
        elif 'blue' in s:
                s= 'blue'
        elif 'blacktip' in s:
                s = 'blacktip'
        elif 'wobbegong' in s or 'wobegong' in s:
                s = 'wobbegong'
        elif 'no shark involvement' in s or 'questionable' in s or 'unknown' in s or 'or' in s or 'unidentified' in s:
                s = 'no information'
        elif 'bull' in s:
                s = 'bull'
        elif 'tiger' in s:
                s = 'tiger'
        elif 'nurse' in s:
                s = 'nurse'
        elif 'lemon' in s:
                s = 'lemon'
        elif 'whaler' in s:
                s = 'whaler'
        elif len(str(s))>10 and 'identified' not in s:
                s = 'no information'
        elif 'sand' in s:
                s = 'sand'
        elif 'toshark' in s:
                s = 'no information'
        elif 'leopard' in s:
                s = 'leopard'
        elif 'reef shark' in s:
                s = 'reef'
        elif 'dog' in s:
                s = 'dog'
        elif 'gray' in s or 'grey' in s:
                s = 'gray'
        elif 'foot shark' in s:
                s = 'foot'

        elif 'tokg' in s:
                s = 'no information'

        elif 'hammerhead' in s:
                s = 'hammerhead'
        elif 'dusky' in s:
                s = 'dusky'
        elif 'cow' in s:
                s = 'cow'
        elif 'whale' in s:
                s = 'whale'

        return s

    def finsp(s):
            if 'shark' in s or len(str(s)) <= 2 or  ' ' in s:
                s = 'no information'
            return s
    dfs.Species = dfs.Species.apply(comsp)
    dfs.Species = dfs.Species.apply(finsp)
    dfs.Species = dfs.Species.apply(lambda s: re.sub('.[0-9]+.|[0-9]', '', s) )
    dfs.Species = dfs.Species.apply(lambda s: re.sub('m\s|.lb.|\]|\[|\skg\s|\"', '', s) )


    return  dfs

# Case Number
def casenumb_col(dfs):
    dfcn = dfs.rename(columns = {'Case Number':'Case_Number'})
    dfcn.Case_Number.fillna('no information', inplace = True)

    return dfcn


##Unnamed: 23, Unnamed:22, original order, case number.2, case number.1,  href, href formula, pdf#############################################
def many_cols(dfcn):
    dfcn['Unnamed: 22'].fillna('No information', inplace = True)
    dfcn['Unnamed: 23'].fillna('no information', inplace = True)
    dfcn['Case Number.2'].fillna('no information', inplace = True)
    dfcn['Case Number.1'].fillna('no information', inplace = True)
    dfcn['href'].fillna('No information', inplace = True)
    dfcn['href formula'].fillna('No information', inplace = True)
    dfcn['pdf'].fillna('No information', inplace = True)
    dfcn['original order'].fillna('No information', inplace = True)
    return dfcn

##Investigator or Source¨**************************************************************************************************
def sour_col(dfcn):
    dfis = dfcn.rename(columns = {'Investigator or Source':'Investigator_or_Source'})
    esp_1 = lambda x: re.sub('^\s', "", str(x))
    esp_2 = lambda x: re.sub('\s$', "", str(x))
    dfis.Investigator_or_Source = dfis.Investigator_or_Source.apply(esp_1)
    dfis.Investigator_or_Source = dfis.Investigator_or_Source.apply(esp_1)
    dfis.Investigator_or_Source.fillna('No information', inplace = True)
    dfis.Investigator_or_Source = dfis.Investigator_or_Source.str.replace('  ', ' ')
    dfis.Investigator_or_Source = dfis.Investigator_or_Source.str.replace('\,\s[0-9]\/\d{2}\/\d{4}|\,\s[0-9]\/\d{1}\/\d{4}|\,\s[0-9]\/\d{2}\/\d{2}|', '')
    dfis.Investigator_or_Source = dfis.Investigator_or_Source.str.replace('\,\s\d{2}\/\d{2}\/\d{3}\.\.\.', '')

    return dfis

# Time******************************************************************************************************+
def time_col(dfis):
    dfis.Time.fillna('No information', inplace = True)

    def timem(s):
        t = re.findall('\d{2}h\d{2}', s)
        if t != []:
            s = t[0]
        else:
            s = 'No information'
        return s

    dfis.Time = dfis.Time.apply(timem)

    return dfis

#Injury **************************************************************************************************************
def inju_col(dfis):
    dfis.Injury.fillna('No information', inplace = True)
    def inj(s):
        if 'No' in s or 'no' in s:
            s = 'No injury'

        return s

    def nofat(s):
        if 'fatal' == s.lower():
            s = 'No information'

        return s

    def repfat(s):
        s = s.replace('FATAL,', '')
        return s.rstrip().lstrip()

    dfis.Injury = dfis.Injury.apply(repfat)
    dfis.Injury = dfis.Injury.apply(nofat)
    dfis.Injury = dfis.Injury.apply(inj)

    return dfis

#Names*********************************************************++
def names_col(dfis):
    dfn  = dfis.rename(columns = {'Case Number':'Case_Number'})
    dfn.Name.fillna('No information', inplace = True)
    def cap(s):
        t = re.findall('[A-Z]',str(s))
        if t == []:
            return 'No information'
        else:
            return s

    def cap_es(s):
        t = str(s).split(' ')
        s = ''
        for e in t:
            a = re.findall('[A-Z]', e)
            if a != []:
                s = s+ ' ' + e
        if s == '':
            s='No information'

        return str(s).lstrip()

        dfn.Name = dfn.Name.apply(cap_es)

    def quitpr(s):
            if len(str(s))<=3 or 'Japanese' in s or 'Indian' in s or 'Anonymous' in s or 'American' in s or 'Arab' in s or 'Fijian' in s or'French' in s or 'German' in s or 'Zulu' in s or 'Unknown' in s or 'Russian' in s or 'Hindu' in s or 'African' in s or 'M.C.' in s or 'Malay' in s or 'US' in s or 'Fishing' in s:
                s = 'No information'
            elif 'Unidentified' in s or 'Swedish' in s or 'Spain' in s or 'Somali' in s or 'Aboriginal' in s or 'English' in s:
                s = 'No information'
            elif 'B.T.' in s or 'Cuba' in s or 'Danish' in s or 'Teazer' in s:
                s = 'No information'
            return s
    dfn.Name = dfn.Name.apply(quitpr)

    return dfn

#Date **********************************************************************************************
def dates_col(dfn):
    dfdat  = dfn.rename(columns = {'Case Number':'Case_Number'})
    dfdat.Date.fillna('No information', inplace = True)

    def nshf(s):
        if len(str(s)) <5 or 'No' in s or 'no' in s or 'Re' in s or 'Bef' in s :
            s = 'No information'
        return s
    dfdat.Date = dfdat.Date.apply(nshf)

    def fech(s):
        t = re.findall('\d{1,}-\w{1,}-\d{2}',s)
        if t == []:
            s = 'No information'
        return s.rstrip().lstrip()
    dfdat.Date = dfdat.Date.apply(fech)

    def sho(s):
        if len(s)>11 or len(s)<2 or ' ' in s:
                s= 'No information'
        return s
    dfdat.Date = dfdat.Date.apply(sho)

    def form(s):
        try:
            t = s.split('-')
            if t[1] == '01' or t[1] == '1':
                t[1] = 'Jan'
            if t[1] == '02' or t[1] == '2':
                t[1] = 'Feb'
            if t[1] == '03' or t[1] == '3':
                t[1] = 'Mar'
            if t[1] == '04' or t[1] == '4':
                t[1] = 'Apr'
            if t[1] == '05' or t[1] == '5':
                t[1] = 'May'
            if t[1] == '06' or t[1] == '6':
                t[1] = 'Jun'
            if t[1] == '07' or t[1] == '7':
                t[1] = 'Jul'
            if t[1] == '08' or t[1] == '8':
                t[1] = 'Aug'
            if t[1] == '09' or t[1] == '9':
                t[1] = 'Sep'
            if t[1] == '10':
                t[1] = 'Oct'
            if t[1] == '11':
                t[1] = 'Nov'
            if t[1] == '12':
                t[1] = 'Dec'

            if len(str(t[2])) == 2 and int(t[2]) < 19:
                    t[2] = '20'+str(t[2])
                    #print(t[2], int(t[2]) < 19)
            elif len(str(t[2])) == 2 and int(t[2]) >= 19:
                    t[2] = '19'+str(t[2])
                    #print(t[2], int(t[2]) >= 19)
            s = str(t[0]) +'-'+str(t[1]).capitalize()+'-'+str(t[2])
            #print(s)

            return s
        except:
            pass
    dfdat.Date = dfdat.Date.apply(form)
    return dfdat

#Year *****************************************************+
def  year_col(dfdat):
    dfyea  = dfdat.rename(columns = {'Case Number':'Case_Number'})
    dfyea.Year.fillna('No information', inplace = True)
    def nolet(s):
        t = re.findall('0s', str(s))
        if t != []:
            s = 'No information'
        return str(s).rstrip().lstrip()
    dfyea.Year = dfyea.Year.apply(nolet)

    def formy(s):
        s = str(s)
        if len(s) == 3:
            s = '0'+'s'
        elif len(s) == 2 and int(s)<19 :
            s = '20'+s
        elif len(s) == 2 and int(s)>=19 :
            s = '19' + s
        elif len(s) == 1:
            s = '000' + s
        return s
    dfyea.Year = dfyea.Year.apply(formy)

    return dfyea

#Area
def area_col(dfyea):
    dfar =dfyea.rename(columns = {'Case Number':'Case_Number'})
    dfar.Area.fillna('No information', inplace = True)
    def noesps(s):
        return s.rstrip().lstrip()
    dfar.Area = dfar.Area.apply(noesps)

    def unknown(s):
        if 'unknown' in s or 'Unknown' in s:
            s = 'No information'

        return s
    dfar.Area = dfar.Area.apply(unknown)

    return dfar

#Location
def location_col(dfar):
    dfar.Location.fillna('No information', inplace = True)
    def nonum(s):
        t = re.findall('\d',s)
        if t != []:
            s = 'No information'
        return s
    dfar.Location = dfar.Area.apply(nonum)
    return dfar

#Guardar
def salvar(dfar):
    final = dfar.to_csv('limpio.csv', index=False)

#imprimir
def datos_im(df):
    t =['Sex', 'Age', 'Fatal (Y/N)', 'Time', 'Species']
    for e in t:
        print(df[e].value_counts())
