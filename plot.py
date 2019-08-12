import matplotlib.pyplot as plt
import numpy as np

Rtreey=np.array([0.06171875, 0.2296875,  0.6912109375,  0.9630859375,  1.0, 0.999609375, 1.0, 1.0, 1.0, 1.0, 1.0])
VA_ssay=np.array([0.8482142857142857, 0.3052455357142857, 0.09395926339285714, 0.045611926631756665, 0.04289309904321466, 0.021265714285714287, 0.012134285714285714, 0.01453142857142857, 0.014362857142857144, 0.017662857142857143, 0.021434285714285715])
VA_noay=np.array([0.21428571428571427, 0.04966517857142857, 0.033482142857142856, 0.032616737999174264, 0.02986702057687754, 0.013602857142857144, 0.005148571428571429, 0.006002857142857144, 0.006537142857142857, 0.007665714285714287, 0.010954285714285713])
percentage=np.array([100,100,100,100,100,100,100,100,100,100,100])
x=[2,4,6,8,10,14,18,20,22,26,30]

plt.title('N=50,000 uniformly distibuted, k=10,')
plt.plot(x,Rtreey*percentage,color='green',label='R-tree',marker='o')
plt.plot(x,VA_ssay*percentage,color='skyblue',label='VA_SSA',marker='x')
plt.plot(x,VA_noay*percentage,color='blue',label='VA_NOA',marker='*')
plt.legend()
plt.xlabel('Number of dimensions in vectors')
plt.ylabel('% vector/Leaf blocks visited')
plt.show()
