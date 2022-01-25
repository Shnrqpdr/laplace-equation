import numpy as np 
import pandas as pd 

array_file = pd.read_csv("temposThreads.dat", header = 0, sep='\s+')

piorCaso = 282.207

tab = '\t'
i = 1
tempos = array_file['tempo']

print(f'eficiencia{tab}threads{tab}speedup{tab}aceleracao\n')

while(i <= 8):
    eficiencia = (1 - (tempos[i-1])/piorCaso)*100
    speedup = piorCaso/tempos[i-1];
    aceleracao = 1 - tempos[i-1]/((i)*piorCaso);
    print(f'{eficiencia}{tab}{i}{tab}{speedup}{tab}{aceleracao}')
    i = i+1