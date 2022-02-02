import matplotlib.pyplot as plt 
import numpy as np 
import pandas as pd 

df_nopt = pd.read_csv("caso1.txt", header = 0, sep='\s+')
df_I = pd.read_csv("caso2.txt",header = 0, sep='\s+')
df_II = pd.read_csv("caso3.txt", header = 0, sep='\s+')
df_III = pd.read_csv("caso4.txt", header = 0, sep='\s+')
df_IV = pd.read_csv("caso5.txt", header = 0, sep='\s+')

fig = plt.figure(figsize=(8,6))

x=np.arange(0,4,1)

axes = fig.add_axes([0.1,0.1,0.8,0.8])
#axes2 = fig.add_axes([0.4,0.5,0.4,0.3])

axes.plot(df_nopt['O'], df_nopt['t'], color='g', ls='-.', marker='o',markersize=8, label="No optimatizated")
axes.plot(df_I['O'], df_I['t'],color='b', ls='-.', marker='o',markersize=8, label="Optimizated with flags I")
axes.plot(df_II['O'], df_II['t'], color='r', ls='-.', marker='o', markersize=8, label="Optimizated with flags II")
axes.plot(df_III['O'], df_III['t'], ls='-.', marker='o', markersize=8, label="Optimizated with flags III")
axes.plot(df_IV['O'], df_IV['t'], ls='-.', marker='o', markersize=8, label="Optimizated with flags IV")
axes.set_xlabel('Flags O(X)')
axes.set_ylabel("Time (s)")

axes.set_title("Comparison of optimatizations for each case")
plt.grid(linestyle='-', linewidth=0.5)
axes.legend(loc='upper right')

plt.savefig("BenchmarkFlags.pdf",dpi=600)