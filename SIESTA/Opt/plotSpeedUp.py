import matplotlib.pyplot as plt 
import numpy as np 
import pandas as pd 

array_file = pd.read_csv("eficienciaThreads.dat", header = 0, sep='\s+')

fig = plt.figure(figsize=(8,6))

x=np.arange(0,4,1)

axes = fig.add_axes([0.1,0.1,0.8,0.8])

arrayreta = [1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7]
arraythreads = [1,2,3,4,5,6,7,8]

axes.plot(array_file['threads'], array_file['speedup'], ls='-', marker='o',markersize=6, label=f'Speedup per thread')    
axes.plot(arraythreads, arrayreta, ls='-', label=f'Reference')          

    
axes.set_xlabel('Number of Threads')
axes.set_ylabel("Speedup")
axes.set_title("Perfomance comparison for each Thread - SpeedUp")
axes.legend(loc='lower right')

#plt.show()
plt.grid(linestyle='-', linewidth=0.5)
plt.savefig("plotSpeedUpSiestaOPTLab107.pdf",dpi=600)