import matplotlib.pyplot as plt
import numpy as np

Rtreey=np.array([0.11796875, 0.47890625, 0.8677734375, 0.9873046875, 1.0, 1.0, 1.0, 1.0, 1.0,1.0,1.0])
VA_ssay=np.array([0.9017857142857143, 0.3861607142857143, 0.11884142347718506, 0.05204634784260436, 0.06952176669933163, 0.03775142857142857, 0.015505714285714286, 0.02112857142857143, 0.027780000000000003, 0.03608571428571428, 0.042668571428571424])
VA_noay=np.array([0.16964285714285715, 0.07756696428571429, 0.04431991849210393, 0.03619281403877906, 0.05060844819164526, 0.022745714285714286, 0.0057542857142857135, 0.009694285714285714, 0.013977142857142856, 0.01884571428571429, 0.024742857142857143])
percentage=np.array([100,100,100,100,100,100,100,100,100,100,100])
x=[2,4,6,8,10,14,18,20,22,26,30]

plt.title('N=50,000 Beta distibuted, k=10,')
plt.plot(x,Rtreey*percentage,color='green',label='R-tree',marker='o')
plt.plot(x,VA_ssay*percentage,color='skyblue',label='VA_SSA',marker='x')
plt.plot(x,VA_noay*percentage,color='blue',label='VA_NOA',marker='*')
plt.legend()
plt.xlabel('Number of dimensions in vectors')
plt.ylabel('% vector/Leaf blocks visited')
plt.show()
