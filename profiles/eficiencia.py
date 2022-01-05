import numpy as np 
import pandas as pd 

df_nopt = pd.read_csv("profilesTempo.txt", header = 0, sep='\s+')

piorCaso = 127.55

tab = '\t'
i = 0
noOpt = df_nopt['t']

print('tipo\tt\n')

while(i < 3):
    eficiencia = (1 - (noOpt[i])/piorCaso)*100
    print(f'{i}{tab}{eficiencia}')
    i = i+1
    
