# _*_ coding: utf-8 _*_

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

d = np.random.rand(300,4)
# ndarray是多维数组，不是numpy的特殊格式
data = pd.DataFrame(data=d,columns=list('梅兰竹菊'))
print('='*50)
print(data)
# 保存到csv文件
data.to_csv('data.csv',index=False,header=True)
print('保存成功！')