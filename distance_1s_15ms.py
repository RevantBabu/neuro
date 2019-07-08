import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def vanRossumDistance(u, v, tau):
  componentU = 0;
  for i in range(0, u.shape[0]):
    for j in range(0, u.shape[0]):
      componentU += np.exp(-abs(u[i]-u[j])/tau)

  componentV = 0;
  for i in range(0, v.shape[0]):
    for j in range(0, v.shape[0]):
      componentV += np.exp(-abs(v[i]-v[j])/tau)

  componentUV = 0;
  for i in range(0, u.shape[0]):
    for j in range(0, v.shape[0]):
      componentUV += np.exp(-abs(u[i]-v[j])/tau)

  return componentU + componentV - 2*componentUV


def generateDistanceMatrix(n, tau):
  result = np.zeros(shape=(n,n))
  for i in range(0, n):
    print(i)
    for j in range(i+1, n):
      result[i][j] = vanRossumDistance(np.asarray(n1counts[i] if (i in n1counts) else []), np.asarray(n1counts[j] if (j in n1counts) else []), tau)
  
  for i in range(0, n):
    for j in range(0, i):
      result[i][j] = result[j][i]

  return result  


df1 = pd.read_csv("data/N1.csv", header=None)
n1 = df1[0].values
start = 7946
end = 8882
slots = end-start
n1counts = {}

for spike_time in n1:
	key = int(spike_time-start)
	if (key in n1counts):
		n1counts[key].append(int((spike_time-int(spike_time))*1000))
	else:
		n1counts[key] = [int((spike_time-int(spike_time))*1000)]

d = generateDistanceMatrix(slots, 15)

np.save("distance_matrix_1s_15ms.npy", d)
print(d.shape)