# Dimensionality Reduction on Neuronal Data
---
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
 - ![equation](http://www.sciweavers.org/tex2img.php?eq=d_%7Bij%7D%20%3D%20%20%5Csurd%20d1_%7Bij%7D%5E%7B2%7D%20%2B%20%20d2_%7Bij%7D%5E%7B2%7D&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0)

 where d1 is distance matrix for neuron1 and d2 is for neuron2
 
 ### Laplacian and Eigen values
 
 ### Results