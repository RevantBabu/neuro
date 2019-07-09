import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/pos.csv", header=None)
df.columns = ['timestamp', 'xpos', 'ypos']

xpos = {}
ypos = {}

for index, row in df.iterrows():
	key = int(row['timestamp']) - 7946
	if (key in xpos):
		xpos[key].append(row['xpos'])
		ypos[key].append(row['ypos'])
	else:
		xpos[key] = []
		ypos[key] = []


n = 936
result = np.zeros(shape=(n,n))

for i in range(0, n):
	xpos[i] = np.mean(xpos[i])
	ypos[i] = np.mean(ypos[i])

for i in range(0, n):
	print(i)
	for j in range(i+1, n):
		result[i][j] = np.sqrt((xpos[i]-xpos[j])**2 + (ypos[i]-ypos[j])**2)

for i in range(0, n):
	for j in range(0, i):
  		result[i][j] = result[j][i]

d = []
for i in range(0,n):
	for j in range(0,n):
		d.append(result[i][j])

d = np.asarray(d)

fig = plt.figure(figsize=(9,9))
ax = plt.subplot(111)
ax.hist(d, bins=np.arange(d.min(), d.max()+1), align='left')
plt.title('distance distribution')
plt.xlabel('distance')
plt.ylabel('frequency')
plt.savefig("distance_distribution_pos.png")