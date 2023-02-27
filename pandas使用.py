



#练习1
#第一题和第二题采用学生数据集：
import pandas as pd
stu_dic = {'Age':[14,13,13,14,14,12,12,15,13,12,11,14,12,15,16,12,15,11,15],
'Height':[69,56.5,65.3,62.8,63.5,57.3,59.8,62.5,62.5,59,51.3,64.3,56.3,66.5,72,64.8,67,57.5,66.5],
'Name':['Alfred','Alice','Barbara','Carol','Henry','James','Jane','Janet','Jeffrey','John','Joyce','Judy','Louise','Marry','Philip','Robert','Ronald','Thomas','Willam'],
'Sex':['M','F','F','F','M','M','F','F','M','M','F','F','F','F','M','M','M','M','M'],
'Weight':[112.5,84,98,102.5,102.5,83,84.5,112.5,84,99.5,50.5,90,77,112,150,128,133,85,112]}
student = pd.DataFrame(stu_dic)
#1．查询Name,Height,Weight列的前五行；查询第1，3，5，6，8行信息。
print(student[['Name','Height','Weight']].head(5))
print("第一行信息：")
print(student.loc[0])
print("第三行信息：")
print(student.loc[2])
print("第五行信息：")
print(student.loc[4])
print("第六行信息：")
print(student.loc[5])
print("第八行信息：")
print(student.loc[7])
#2．查询所有12岁以上的女生姓名、身高、体重；删除1，3，5，6行数据。
a = student.loc[student["Age"]>12]
print(a[['Name','Height','Weight']])
print("--------------------------------------------")
print(student)
print(student.drop([0,2,4,5]))#删除
print("--------------------------------------------")
#3．随机生成均值为3，方差为4，大小100的正态分布，输出它的描述性统计指标。（提示：numpy.random.normal()）
import numpy as np
data = np.random.normal(3,4,100)#参数为均值、方差、大小
print(data.sum())
print(data.mean())

#练习2
#以下三题采用学生数据集，如下：
import pandas as pd

stu_dic = {'Age':[14,13,13,14,14,12,12,15,13,12,11,14,12,15,16,12,15,11,15],
'Height':[69,56.5,65.3,62.8,63.5,57.3,59.8,62.5,62.5,59,51.3,64.3,56.3,66.5,72,64.8,67,57.5,66.5],
'Name':['Alfred','Alice','Barbara','Carol','Henry','James','Jane','Janet','Jeffrey','John','Joyce','Judy','Louise','Marry','Philip','Robert','Ronald','Thomas','Willam'],
'Sex':['M','F','F','F','M','M','F','F','M','M','F','F','F','F','M','M','M','M','M'],
'Weight':[112.5,84,98,102.5,102.5,83,84.5,112.5,84,99.5,50.5,90,77,112,150,128,133,85,112]}
student = pd.DataFrame(stu_dic)
#1.按照性别分类，计算各组别中学生身高和体重的平均值
group = student.groupby('Sex')
g1 = group.get_group('M')#得到女生分组
print("女生组别身高均值：",g1['Height'].mean())
print("女生组别体重均值：",g1['Weight'].mean())
g2 = group.get_group('F')#得到男生分组
print("男生组别身高均值：",g2['Height'].mean())
print("男生组别体重均值：",g2['Weight'].mean())
print("------------------------------------------")
#2.按照性别与年龄一起分类，计算各组别身高和体重的平均值和中位数
group = student.groupby(['Sex','Age'])
for i in group:
    print(i[0])
    print("身高均值：",group.get_group(i[0])['Height'].mean())
    print("身高中位数：",group.get_group(i[0])['Height'].median())
    print("体重均值：",group.get_group(i[0])['Weight'].mean())
    print("体重中位数：",group.get_group(i[0])['Weight'].median())
#3.按照学生的年龄升序排序，年龄一样则按照身高降序排序
student.sort_values(by=['Age','Height'],ascending=[False,True])
