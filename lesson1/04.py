# _*_ coding: utf-8 _*_

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

x = np.arange(0,10,0.1)
y = x**x
plt.plot(x,y,'r-',lw=3)
plt.show()