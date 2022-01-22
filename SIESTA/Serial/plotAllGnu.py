import matplotlib.pyplot as plt 
import numpy as np 
import pandas as pd 

df_nopt = pd.read_csv("plot.txt", header = 0, sep='\s+')

fig = plt.figure(figsize=(8,6))

x=np.arange(0,4,1)

axes = fig.add_axes([0.1,0.1,0.8,0.8])
#axes2 = fig.add_axes([0.4,0.5,0.4,0.3])

axes.plot(df_nopt['O'], df_nopt['t'], color='g', ls='-.', marker='o',markersize=8)
axes.set_xlabel('Casos: 1-3')
axes.set_ylabel("Eficiência (%)")
axes.set_title("Comparação da eficiência para cada caso")
axes.legend(loc='upper right')


#plt.show()
plt.savefig("profilesEficiencia.pdf",dpi=300)
