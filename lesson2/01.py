# _*_ coding: utf-8 _*_

import matplotlib.pyplot as plt

def first_digital(x):
    while x>=10:
        x//=10
    return x

if __name__ == '__main__':
    n=1
    # 生成一维数组的一种方法
    frequence = [0]*9
    print(frequence)
    for i in range(1,1000):
        n*=i
        index = first_digital(n)-1
        frequence[index]+=1
    print(frequence)
    plt.plot(frequence,'r-',lw=3)
    plt.grid(True)
    plt.show()