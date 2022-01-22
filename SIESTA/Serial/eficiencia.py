import numpy as np 
import pandas as pd 

df_nopt = pd.read_csv("Lab107/noFlagGnu.txt", header = 0, sep='\s+')
df_I = pd.read_csv("Lab107/nativeGnu.txt",header = 0, sep='\s+')
df_II = pd.read_csv("Lab107/i7avxGnu.txt", header = 0, sep='\s+')

piorCaso = 999.389

tab = '\t'
i = 0
noOpt = df_nopt['t']
optI = df_I['t']
optII = df_II['t']

print('Nao otimizado\n')

while(i < 4):
    eficiencia = (1 - (noOpt[i])/piorCaso)*100
    print(f'{i}{tab}{eficiencia}')
    i = i+1
    
i = 0

print('Otimizado I\n')

while(i < 4):
    eficiencia = (1 - (optI[i])/piorCaso)*100
    print(f'{i}{tab}{eficiencia}')
    i = i+1
    
i = 0

print('Otimizado II\n')

while(i < 4):
    eficiencia = (1 - (optII[i])/piorCaso)*100
    print(f'{i}{tab}{eficiencia}')
    i = i+1