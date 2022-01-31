import numpy as np 
import pandas as pd 

array_file = pd.read_csv("temposThreadsPessoal.txt", header = 0, sep='\s+')

piorCaso = 2992.940000

tab = '\t'
i = 0
t = 1
opt = array_file['tempos']

print(f'threads{tab}eficiencia')

while(i < 8):
    eficiencia = (1 - (opt[i])/piorCaso)*100
    t = t + 1
    print(f'{t} {eficiencia}')
    i = i+1
