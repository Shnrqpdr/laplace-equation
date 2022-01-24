import numpy as np 
import pandas as pd 

array_file = pd.read_csv("temposThreads.dat", header = 0, sep='\s+')

piorCaso = 282.207

tab = '\t'
i = 1
tempos = array_file['tempo']

print(f'eficiencia{tab}threads{tab}speedup\n')

while(i <= 8):
    eficiencia = (1 - (tempos[i-1])/piorCaso)*100
    speedup = piorCaso/tempos[i-1];
    print(f'{eficiencia}{tab}{i}{tab}{speedup}')
    i = i+1