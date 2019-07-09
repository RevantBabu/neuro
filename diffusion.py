import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def generateSimilarityMatrix(dM):
  n = dM.shape[0]
  m = dM.shape[1]
  result = np.zeros(shape=(n,m))
  for i in range(0, n):
    for j in range(0, m):
      if (i==j): result[i][j] = 0
      elif (dM[i][j]==0): result[i][j] = 1 #because some slots have 0 spikes? 
      # is default 1 fine? if 0 used, gives imaginary eVs
      else: result[i][j] = 1/dM[i][j]
  return result

def thresholdMatrix(sM, topN):
  n = sM.shape[0]
  m = sM.shape[1]
  result = np.zeros(shape=(n,m))

  columnSorted = np.sort(sM,axis=0)
  rowSorted = np.sort(sM,axis=1)

  rowTopN = np.zeros(n)
  columnTopN = np.zeros(n)

  for i in range(0, n):
    rowTopN[i] = rowSorted[i, :][n-topN]
    columnTopN[i] = columnSorted[:, i][n-topN]


  for i in range(0, n):
    for j in range(0, m):
      if (sM[i][j]>=rowTopN[i] or sM[i][j]>=columnTopN[j]):
        result[i][j] = sM[i][j]
  
  return result

def generateLaplacianMatrix(tM):
  n = tM.shape[0]
  m = tM.shape[1]
  result = np.zeros(shape=(n,m))
  columnSums = np.sum(tM, axis = 0)
  for i in range(0, n):
    for j in range(0, m):
      if (i==j): result[i][j] = 1
      else: result[i][j] = -tM[i][j]/columnSums[j]
  return result


d1 = np.load("distance_matrix1_1s_15ms.npy")
d2 = np.load("distance_matrix2_1s_15ms.npy")
dM = np.sqrt(d1**2 + d2**2)
sM = generateSimilarityMatrix(dM)
tM = thresholdMatrix(sM, 10)
lM = generateLaplacianMatrix(tM)


w, v = np.linalg.eig(lM)
idx = w.argsort()[::-1]

wSorted = w[idx]
vSorted = v[idx]
print("eigenValues")
print(wSorted , "\n")

print("eigenVectors")
print(vSorted, "\n")

np.savetxt('eigenValues.txt', wSorted)
np.savetxt('eigenVectors.txt', vSorted)