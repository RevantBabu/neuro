# Dimensionality Reduction on Neuronal Data

## Data

Currently using data from [hc-13](https://crcns.org/data-sets/hc/hc-13/about-hc-13)

Filtered data consists of:
- data/N1.csv : spike timings from neuron 1(ms resolution)
- data/N4.csv : spike timings from neuron 4(ms resolution)
- data/pos.csv : timestamp, xpos, ypos

The above data is filtered for \[Animal Q1\] \[Day 14\] \[Epoch 6\] \[Tetrode 27\]. Below is few information on this session:
- startTime: 7946sec; endTime: 8882sec; Total: 936 secs
- Number of spikes in N1 : 11717
- Number of spikes in N4: 26161
- There were 5 other neurons but spikes were in order of 100, so were not considered for now
- The pos.csv is plotted below, showing the path taken by animal

![position plot](https://github.com/RevantBabu/neuro/blob/master/position_plot.png?raw=true)

## DiffusionMap

### Distance Matrix

__1s_inf__

- For each neuron N_i \[startTime:endTime\] is divided into 1sec intervals, giving 936 points. Distance between spike trains of 1sec interval are calucated using vanRossum metric with Tau=Infinity

__1s_15ms__

- For each neuron N_i \[startTime:endTime\] is divided into 1sec intervals, giving 936 points. Distance between spike trains of 1sec interval are calucated using vanRossum metric with Tau=15ms
- Current method takes __~45mins__ for 936 points

 
 Final distance matrix d for both neurons combined is arrived by: 
 
    d_ij = sqrt( d1_ij^2 + d2_ij^2 )
    
 where d1 is distance matrix for neuron1 and d2 is for neuron2
 
 ### Laplacian and Eigen values
 **Eigen Values**
```python
#top 5 eigenValues for 1s_inf
1.480848230250900954e+00
1.453581974646489083e+00
1.414983182478089407e+00
1.379302645289375073e+00
1.366143674708713451e+00

#top 5 eigenValues for 1s_15s: neuron1
1.621338730825693908e+00
1.372961018632574248e+00
1.369770579632879404e+00
1.367424801952719982e+00
1.365294349138670649e+00

#top 5 eigenValues for 1s_15s: neuron1 & neuron4
1.379449029829036943e+00
1.372827343884797768e+00
1.370727056567152768e+00
1.369143754727786044e+00
1.366893634827345050e+00
```

**Leading EigenVector**

**1s_inf**

![1s_inf](https://github.com/RevantBabu/neuro/blob/master/results/1s_inf/leadingVector.png?raw=true)
**1s_15ms neuron1**

![1s_15ms_n1](https://github.com/RevantBabu/neuro/blob/master/results/1s_15ms/n1/leadingVector.png?raw=true)

**1s_15ms both neurons**

![1s_15ms_n1n2](https://github.com/RevantBabu/neuro/blob/master/results/1s_15ms/n1n2/leadingVector.png?raw=true)

**Distance Distributions**

**1s_15ms n1**
![n1](https://github.com/RevantBabu/neuro/blob/master/results/distances/distance_distribution_n1.png?raw=true)

**1s_15ms n2**
![n2](https://github.com/RevantBabu/neuro/blob/master/results/distances/distance_distribution_n2.png?raw=true)

**1s_15ms n1n2**
![n1n2](https://github.com/RevantBabu/neuro/blob/master/results/distances/distance_distribution_n1n2.png?raw=true)

**1s_15ms pos**
![pos](https://github.com/RevantBabu/neuro/blob/master/results/distances/distance_distribution_pos.png?raw=true)
 ### Results