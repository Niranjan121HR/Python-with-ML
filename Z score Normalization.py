import numpy as np
dataset=[10,20,30,40,50]
mean=np.mean(dataset)
std=np.std(dataset)
for v in dataset:
    z_score=(v-mean)/std
    print(v,"=",z_score)