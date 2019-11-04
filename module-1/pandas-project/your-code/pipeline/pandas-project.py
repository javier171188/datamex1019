from funciones import *


#leer el archivo
arc = "attacksu.csv"
df = leer(arc)

#Atacamos la columna    type
df = type_col(df)

#Country
df = country_col(df)


#Sex
df = sex_col(df)

#Fatal
df = fatal_col(df)

#Activity
df = activity_col(df)

#Age
df = age_col(df)

#Species
df = species_col(df)

###Case Number
df = casenumb_col(df)

#Unnamed: 23, Unnamed:22, original order, case number.2, case number.1,  href, href formula, pdf
df = many_cols(df)

##Investigator or Source
df = sour_col(df)

#Time
df = time_col(df)

#Injury
df = inju_col(df)

#Names
df = names_col(df)

#Dates
df = dates_col(df)

#Year
df = year_col(df)

#Area
df = area_col(df)

#Location
df = location_col(df)


#Guardamos el trabajo
salvar(df)

#imprimimos lo más importante
datos_im(df)
