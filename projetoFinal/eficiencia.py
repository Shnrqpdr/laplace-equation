import numpy as np 
import pandas as pd 

df_nopt = pd.read_csv("caso1.txt", header = 0, sep='\s+')
df_I = pd.read_csv("caso2.txt",header = 0, sep='\s+')
df_II = pd.read_csv("caso3.txt", header = 0, sep='\s+')
df_III = pd.read_csv("caso4.txt", header = 0, sep='\s+')
df_IV = pd.read_csv("caso5.txt", header = 0, sep='\s+')

piorCaso = 8492

tab = '\t'
i = 0
noOpt = df_nopt['t']
optI = df_I['t']
optII = df_II['t']
optIII = df_III['t']
optIV = df_IV['t']

print('Nao otimizado\n')

print(f'O{tab}t')

while(i < 4):
    eficiencia = (1 - (noOpt[i])/piorCaso)*100
    print(f'{i}{tab}{eficiencia}')
    i = i+1
    
i = 0

print('Otimizado I\n')

print(f'O{tab}t')

while(i < 4):
    eficiencia = (1 - (optI[i])/piorCaso)*100
    print(f'{i}{tab}{eficiencia}')
    i = i+1
    
i = 0

print('Otimizado II\n')

print(f'O{tab}t')

while(i < 4):
    eficiencia = (1 - (optII[i])/piorCaso)*100
    print(f'{i}{tab}{eficiencia}')
    i = i+1
    
i = 0
print('Otimizado III\n')

print(f'O{tab}t')

while(i < 4):
    eficiencia = (1 - (optIII[i])/piorCaso)*100
    print(f'{i}{tab}{eficiencia}')
    i = i+1
    
i = 0
print('Otimizado IV\n')

print(f'O{tab}t')

while(i < 4):
    eficiencia = (1 - (optIV[i])/piorCaso)*100
    print(f'{i}{tab}{eficiencia}')
    i = i+1