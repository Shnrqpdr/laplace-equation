import matplotlib.pyplot as plt 
import numpy as np 
import pandas as pd 

array_file = pd.read_csv("resultadosOptStatic.dat", header = 0, sep='\s+')

fig = plt.figure(figsize=(10,10))

x=np.arange(0,4,1)

axes = fig.add_axes([0.1,0.1,0.8,0.8])

it = 1
array_time = []
array_chunck = []                     

while (it <= 8):
    array_time = array_file['T'][np.where(array_file['NT'] == it)[0]]  
    array_chunck = array_file['CH'][np.where(array_file['NT'] == it)[0]]
    
    axes.plot(array_chunck, array_time, ls='-', marker='o',markersize=1, label=f'{it} Threads')
    
    it = it + 1
    

axes.set_xlabel('Number of Chuncks')
axes.set_ylabel("Time (seconds)")
axes.set_title("Perfomance comparison for each Thread")
axes.legend(loc='upper left')

#plt.show()
plt.grid(linestyle='-', linewidth=0.5)
plt.savefig("plotPi_static.pdf",dpi=1200)