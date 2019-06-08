# _*_ coding: utf-8 _*_

import numpy as np
import matplotlib.pyplot as plt

# 正态分布
# p = np.random.uniform(0,255,size=(5,5))
# print(p)

# p = np.random.rand(10000)
# hist是直方图的简写 bins显示柱的个数
# plt.hist(p, bins=100,color='g' ,edgecolor='k')
# plt.show()

N = 10000
times = 100

# 生成10000个元素的一维数组
z = np.zeros(N)

for i in range(times):
    # 随机生成10000个元素的随机一维数组
    # 然后和z数组进行相加
    z += np.random.rand(N)
print(z)
z /= times
plt.hist(z,bins=20,color='m',edgecolor='k')
plt.show()