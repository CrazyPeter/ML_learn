# _*_ coding: utf-8 _*_

import numpy as np

a = np.arange(1,10000,1)
# print(a)
pi = np.sqrt(6*np.sum(1/a**2))
print(pi)

# cumprod = 阶乘
x = np.arange(1,20)
e = np.sum(1/x.cumprod())+1
print(e)