import matplotlib.pyplot as plt 
import numpy as np 
import pandas as pd 

df_nopt = pd.read_csv("LNCC/noFlagGnu.txt", header = 0, sep='\s+')
df_I = pd.read_csv("LNCC/nativeGnu.txt",header = 0, sep='\s+')
df_II = pd.read_csv("LNCC/ivybridgeGnu.txt", header = 0, sep='\s+')

fig = plt.figure(figsize=(8,6))

x=np.arange(0,4,1)

axes = fig.add_axes([0.1,0.1,0.8,0.8])
#axes2 = fig.add_axes([0.4,0.5,0.4,0.3])

axes.plot(df_nopt['O'], df_nopt['t'], color='g', ls='-.', marker='o',markersize=8, label="No optimatizated")
axes.plot(df_I['O'], df_I['t'],color='b', ls='-.', marker='o',markersize=8, label="Optimizated with flags I")
axes.plot(df_II['O'], df_II['t'], color='r', ls='-.', marker='o', markersize=8, label="Optimizated with flags II")
axes.set_xlabel('Flags O(X)')
axes.set_ylabel("Time (s)")
axes.set_title("Comparison of optimatizations - GNU Compiler")
axes.legend(loc='upper right')

#axes.arrow(x=2, y=550, dx=0, dy=150, width=.05, facecolor='red', length_includes_head=True, head_width=0.2, head_length=23)
#axes.set_xticks(x)


#axes2.set_xticks([0,1,2,3])
#axes2.set_xlim([0.80,3.3])
#axes2.set_ylim([350,500])
#axes2.grid(True,which="both",ls="-")
#axes2.plot(x,df_nopt, color='r', ls='-.', marker='o', markersize=8)
#axes2.plot(x,df_I,color='y', ls='-.', marker='o',markersize=8, label="OPT I")
#axes2.plot(x,df_II,color='b', ls='-.', marker='o',markersize=8, label="OPT II")
#axes2.set_xlabel('OX')
#axes2.set_ylabel("Time (s)")
#axes2.set_title("Zoom ")

#plt.show()
plt.savefig("GNU-all-LNCC.pdf",dpi=300)