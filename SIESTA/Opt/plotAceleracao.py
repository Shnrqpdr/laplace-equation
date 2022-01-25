import matplotlib.pyplot as plt 
import numpy as np 
import pandas as pd 

array_file = pd.read_csv("eficienciaThreads.dat", header = 0, sep='\s+')

fig = plt.figure(figsize=(8,6))

x=np.arange(0,4,1)

axes = fig.add_axes([0.1,0.1,0.8,0.8])

axes.plot(array_file['threads'], array_file['aceleracao'], ls='-', marker='o',markersize=6, label=f'Acceleration per thread')             

    
axes.set_xlabel('Number of Threads')
axes.set_ylabel("Acceleration ")
axes.set_title("Perfomance comparison for each Thread - Acceleration")
axes.legend(loc='lower right')

#plt.show()
plt.grid(linestyle='-', linewidth=0.5)
plt.savefig("plotAceleracaoSiestaOPTLab107.pdf",dpi=600)