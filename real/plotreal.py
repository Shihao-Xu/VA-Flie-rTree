import matplotlib.pyplot as plt
import numpy as np

Rtreey=np.array([0.071875, 0.245703125, 0.75859375, 0.9119140625, 0.999609375, 0.9998046875, 1.0, 1.0, 1.0, 1.0, 1.0])
VA_ssay=np.array([0.5085714285714286, 0.13000242541838467, 0.06914054281506417, 0.0486572691562577, 0.028676942515062618, 0.026327797436096114, 0.015756092260355844, 0.017300335656818065, 0.013581348015253647, 0.01608357628765792, 0.02282593474303319])
VA_noay=np.array([0.08571428571428573, 0.02376910016977929, 0.028981695771091942, 0.03011377623650044, 0.020339996841302325, 0.018065564078943216, 0.008358449669150657, 0.008071202703552702, 0.006100315020953753, 0.00953238438232436, 0.014283713765579048])
percentage=np.array([100,100,100,100,100,100,100,100,100,100,100])
x=[2,4,6,8,10,14,18,20,22,26,30]

plt.title('N=50,000 image database, k=10,')
plt.plot(x,Rtreey*percentage,color='green',label='R-tree',marker='o')
plt.plot(x,VA_ssay*percentage,color='skyblue',label='VA_SSA',marker='x')
plt.plot(x,VA_noay*percentage,color='blue',label='VA_NOA',marker='*')
plt.legend()
plt.xlabel('Number of dimensions in vectors')
plt.ylabel('% vector/Leaf blocks visited')
plt.show()

