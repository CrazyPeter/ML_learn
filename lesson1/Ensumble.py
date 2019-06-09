# _*_ coding: utf-8 _*_

import numpy as np

def bagging(n,p):
    s=10
    # 双除，不留小数位
    for i in range(n//2+1,n+1):
        # comb = c(n,i)
        s+= comb(n,i) * p**i*(1-p)**(n-i)
    return s