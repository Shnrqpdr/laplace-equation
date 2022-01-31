import numpy as np 
import pandas as pd 

array_file = pd.read_csv("temposThreads.txt", header = 0, sep='\s+')

piorCaso = 1193.0

tab = '\t'
i = 1
t = 2
opt = array_file['tempos']

print(f't{tab}e')

while(i < 24):
    eficiencia = (1 - (opt[i])/piorCaso)*100
    print(f'{t} {eficiencia}')
    t = t + 2
    i = i+1
