#从已有数组创建数组
import numpy as np
a = np.array([1,1])
b = np.asarray(a)
print(b)
x = [[1,1],[2,2]]#list转为array
y = np.asarray(x)
print(y)
c = np.arange(10,20,1)
print(c)
d = np.linspace(10,20,2).reshape([2,1])#建立等差数列，等比数列为logspace
print(d)

#练习1
x = np.array([[1,2,3,4],[4,5,6,7]])
print(x)
a = x.transpose()[1:3].transpose() #取出x的第2-3列
print(a)
b = x[1] #x的第二行
print(b)
c = x[1][2]#x的第2行第3列
print(c)

#迭代器 numpy.nditer
import numpy as np
a = np.arange(6).reshape(2,3)
print('原始数组是：')
print(a)
print('迭代输出元素：')#以数组顺序迭代输出，与矩阵形式无关，转置后迭代顺序也一样
for x in np.nditer(a,op_flags=['readwrite']):
    x[...]=2*x
    print(x,end=",")
#a的个数相当于外部循环个数，b相当于内部循环个数
a = np.arange(0,60,5)
a = a.reshape(3,4)
print('\n第一个数组为：')
print(a)
print('第二个数组为：')
b=np.array([1,2,3,4],dtype=int)
print(b)
print('修改后的数组为：')
for x,y in np.nditer([a,b]):
    print("%d:%d" %(x,y),end=',')
    
import random
#练习2
a = []
for i in range(12):
    a.append(random.randint(0,100))
b = np.array(a).reshape(3,4)
b = np.random.rand(3,4)#用np随机生成
print('随机生成的数组为:')
print(b)
print('每行的和为:')
print(np.sum(b))#求所有数相加的和
print(np.sum(b,axis=1))#求每行的和
print(np.sum(b,axis=0))#求每列的和
sumnp = []
for i in b:
    sumnp.append(np.sum(i))
sumnp = np.array(sumnp)
print(sumnp)
print('每列的平均值为:')
print(np.average(b,axis=0))
print('每列的最大索引为:')
print(np.argmax(b,axis=0))

#np中矩阵和数组是不同的数据类型
randmat = np.mat(np.random.rand(4,4))#将数组转为矩阵
print(randmat)
print(randmat.I)#矩阵求逆
