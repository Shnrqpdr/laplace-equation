import matplotlib.pyplot as plt 
import numpy as np 
import pandas as pd 

df_nopt = pd.read_csv("Lab107/eficienciaNoFlagIntelLab107.txt", header = 0, sep='\s+')
df_I = pd.read_csv("Lab107/eficienciaNoFastLab107.txt",header = 0, sep='\s+')
df_II = pd.read_csv("Lab107/eficienciaFast2Lab107.txt", header = 0, sep='\s+')

fig = plt.figure(figsize=(8,6))

x=np.arange(0,4,1)

axes = fig.add_axes([0.1,0.1,0.8,0.8])

axes.plot(df_nopt['O'], df_nopt['n'], color='g', ls='-.', marker='o',markersize=8, label="No optimatizated")
axes.plot(df_I['O'], df_I['n'],color='b', ls='-.', marker='o',markersize=8, label="Optimizated with flags I")
axes.plot(df_II['O'], df_II['n'], color='r', ls='-.', marker='o', markersize=8, label="Optimizated with flags II")
axes.set_xlabel('Flags O(X)')
axes.set_ylabel("Efficiency(%)")
axes.set_title("Comparison of efficiency optimatizations - Intel Compiler")
axes.legend(loc='center right')

#plt.show()
plt.savefig("INTEL-eficiencia-all-Lab107.pdf",dpi=300)