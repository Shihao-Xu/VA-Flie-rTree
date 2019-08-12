import numpy as np
import math

realData=np.load('image_data.npy')

print (realData.shape)
dimension=2
lst=[]
for i in range(50000):
    lst.append (tuple(realData[i][:dimension]))
print (lst)