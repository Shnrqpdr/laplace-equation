import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd
# %matplotlib inline

coluna=pd.read_csv("dadosLaplace.dat", header = 0, sep='\s+')

fig = plt.figure(figsize=(10,6))
ax1 = fig.add_subplot(111, projection='3d')

mycmap = plt.get_cmap('rainbow')
ax1.set_title('Potencial Eletrostático')
ax1.set_xlabel('Coordenada $x$')
ax1.set_ylabel('Coordenada $y$')

surf1 = ax1.plot_trisurf(coluna['x'], coluna['y'], coluna['z'], cmap=mycmap)
fig.colorbar(surf1, ax=ax1, shrink=0.5, aspect=5)

plt.savefig('plotImagem.png')