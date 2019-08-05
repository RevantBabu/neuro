import numpy as np
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

e = np.load("ephys.npy").item()
a =  e['TT1']['spike_amplitudes']

a_embedded = TSNE(n_components=3).fit_transform(a)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(a_embedded[:,0], a_embedded[:,1], a_embedded[:,2])
plt.savefig("tSNE_3d.png")