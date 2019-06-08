# _*_ coding: utf-8 _*_

import numpy as np
import matplotlib.pyplot as plt

data = 2*np.random.rand(10000,2)-1
x = data[:,0]
y = data[:,1]

# 矩阵运算后的结果还是矩阵，逻辑判断的每个元素都是true或false
idx = x**2+y**2<1
hole = x**2+y**2<0.25

print(type(idx))
# 数组的索引是数组，这应该是numpy的功能
print(data[idx])

# 在1内，不在0.25
idx = np.logical_and(idx,~hole)

# go是绿色，圆圈的意思
# markersize是圆圈的大小
plt.plot(x[idx],y[idx],'go',markersize=1)
plt.show()
