import matplotlib.pyplot as plt
import numpy as np

Rtreey=np.array([0.11796875, 0.47890625, 0.8677734375, 0.9873046875, 1.0, 1.0, 1.0, 1.0, 1.0,1.0,1.0])
VA_ssay=np.array([0.05683563748079877, 0.006916543762396379, 0.010402507351126026, 0.011268484004130918, 0.009442857142857142, 0.006502857142857143, 0.0047, 0.0036257142857142855, 0.004094285714285714, 0.003851428571428571, 0.004377142857142857])
VA_noay=np.array([0.006451612903225807, 0.0013731373645933988, 0.005930897852939982, 0.007269159140517052, 0.005422857142857143, 0.0032428571428571432, 0.0015714285714285713, 0.0013257142857142858, 0.0014057142857142857, 0.001257142857142857, 0.0015857142857142858])
percentage=np.array([100,100,100,100,100,100,100,100,100,100,100])
x=[2,4,6,8,10,14,18,20,22,26,30]

plt.title('N=50,000 exponential distibuted, k=10,')
plt.plot(x,Rtreey*percentage,color='green',label='R-tree',marker='o')
plt.plot(x,VA_ssay*percentage,color='skyblue',label='VA_SSA',marker='x')
plt.plot(x,VA_noay*percentage,color='blue',label='VA_NOA',marker='*')
plt.legend()
plt.xlabel('Number of dimensions in vectors')
plt.ylabel('% vector/Leaf blocks visited')
plt.show()
