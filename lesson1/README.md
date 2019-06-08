# 第一节：Python基础 - Python及其数学库2

看到01：12：00的位置

* 中心极限定理的demo

```python
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
```

* 直方图的画法

```python
# 正态分布
# p = np.random.uniform(0,255,size=(5,5))
# print(p)

# p = np.random.rand(10000)
# hist是直方图的简写 bins显示柱的个数
# plt.hist(p, bins=100,color='g' ,edgecolor='k')
# plt.show()
```

* ndarray是多维数组，不是numpy的特殊格式
* pandas规范格式方法

```python
data = pd.DataFrame(data=d,columns=list('梅兰竹菊'))
print('='*50)
print(data)
# 保存到csv文件
data.to_csv('data.csv',index=False,header=True)
```

