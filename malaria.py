# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 13:52:33 2022

@author: RICHA
"""
import pandas as pd
import geopandas as gpd
import requests

df = pd.read_excel (r'C:\Users\RICHA\Desktop\major\dataset.xlsx')
print (df)

data_cases = df[['State','PPT']]

country_data = gpd.read_file(r'C:\Users\RICHA\Desktop\major\India_State_Boundary.shp')

country_data.replace('Chhattishgarh','Chhattisgarh',  inplace = True)
country_data.replace('Tamilnadu', 'Tamil Nadu', inplace = True)            
country_data.replace('Telengana','Telangana',  inplace = True)
country_data.replace('Odisha','Orissa',  inplace = True)
country_data.replace('Jammu and Kashmir','Jammu & Kashmir',  inplace = True)
country_data.replace('Ladakh','Jammu & Kashmir',  inplace = True) 
country_data.replace('Andaman & Nicobar','A.N.Islands',  inplace = True)
country_data.replace('Daman and Diu and Dadra and Nagar Haveli','Daman & Diu',  inplace = True)  



 
data_cases.rename(columns = {'State': 'State_Name'}, inplace = True)  

final = country_data.merge(data_cases, on = 'State_Name')

final.to_file(r'C:\Users\RICHA\Desktop\major\ppt.shp')
data_cases.to_csv(r'C:\Users\RICHA\Desktop\major\data.csv')
country_data.to_csv(r'C:\Users\RICHA\Desktop\major\geo.csv')