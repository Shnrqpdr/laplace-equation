import matplotlib.pyplot as plt 
import numpy as np 
import pandas as pd 

array_file = pd.read_csv("temposThreads.dat", header = 0, sep='\s+')

fig = plt.figure(figsize=(8,6))

x=np.arange(0,4,1)

axes = fig.add_axes([0.1,0.1,0.8,0.8])

axes.plot(array_file['threads'], array_file['tempo'], ls='-', marker='o',markersize=6, label=f'Time per thread')             

    
axes.set_xlabel('Number of Threads')
axes.set_ylabel("Time (seconds)")
axes.set_title("Perfomance comparison for each Thread")
axes.legend(loc='upper right')

#plt.show()
plt.grid(linestyle='-', linewidth=0.5)
plt.savefig("plotSiestaOPTLab107.pdf",dpi=600)