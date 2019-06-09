# _*_ coding: utf-8 _*_

from PIL import Image
import numpy as np

a = Image.open('lena.png')
print(a)
b = np.array(a)
print(b)
