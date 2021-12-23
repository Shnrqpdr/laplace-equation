import matplotlib.pyplot as plt 
import numpy as np 
import pandas as pd 

df_nopt = pd.read_csv("LNCC/eficienciaNoFlagGnuLNCC.txt", header = 0, sep='\s+')
df_I = pd.read_csv("LNCC/eficienciaNativeLNCC.txt",header = 0, sep='\s+')
df_II = pd.read_csv("LNCC/eficienciaIvybridgeLNCC.txt", header = 0, sep='\s+')

fig = plt.figure(figsize=(8,6))

x=np.arange(0,4,1)

axes = fig.add_axes([0.1,0.1,0.8,0.8])

axes.plot(df_nopt['O'], df_nopt['n'], color='g', ls='-.', marker='o',markersize=8, label="No optimatizated")
axes.plot(df_I['O'], df_I['n'],color='b', ls='-.', marker='o',markersize=8, label="Optimizated with flags I")
axes.plot(df_II['O'], df_II['n'], color='r', ls='-.', marker='o', markersize=8, label="Optimizated with flags II")
axes.set_xlabel('Flags O(X)')
axes.set_ylabel("Efficiency(%)")
axes.set_title("Comparison of efficiency optimatizations - GNU Compiler")
axes.legend(loc='center right')


#plt.show()
plt.savefig("GNU-eficiencia-all-LNCC.pdf",dpi=300)