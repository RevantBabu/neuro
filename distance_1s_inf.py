import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df1 = pd.read_csv("data/N1.csv", header=None)
df2 = pd.read_csv("data/N2.csv", header=None)

n1 = df1[0].values
n2 = df2[0].values

start = 7946
end = 8882
slots = end-start

n1counts = np.zeros(slots)
n2counts = np.zeros(slots)

for spike_time in n1:
	n1counts[int(spike_time-start)] += 1


for spike_time in n2:
	n2counts[int(spike_time-start)] += 1


s = (slots, slots)
d = np.zeros(s)

for i in range(0, slots):
	print(i)
	for j in range(0, slots):
		d1 = np.sqrt(n1counts[i]**2 + n1counts[j]**2 - 2*n1counts[i]*n1counts[j])
		d2 = np.sqrt(n2counts[i]**2 + n2counts[j]**2 - 2*n2counts[i]*n2counts[j])
		d[i][j] = np.sqrt(d1**2 + d2**2)



np.save("distance_matrix_1s_inf.npy", d)
print(d.shape)