/*
 * 实现k-means算法在waveform.data文件中数据聚类
 * @author beastsam
 * @date 2018.10.17
 */
import random 
import pandas as pd
import numpy as np
import tool

#设置精度小数点后两位
np.set_printoptions(precision=2)

#读取文件
df=pd.read_csv("waveform.data",header = None)

#随机选择三个中心点作为初始质心
i1 = random.randint(0,21)     #列标0-21
j1 = random.randint(0,4998)   #行标0-4999
cent1 = df[i1][j1]

i2 = random.randint(0,21)     
j2 = random.randint(0,4998)   
cent2 = df[i2][j2]

i3 = random.randint(0,21)     #列标0-21
j3 = random.randint(0,4998)   #行标0-4999
cent3 = df[i3][j3]

#聚类存储列表
list1 = []
list2 = []
list3 = []

result = 1

while result:
	list1.clear
	list2.clear
	list3.clear
	result = tool.circle (df,cent1,cent2,cent3,list1,list2,list3,result)
	

print("聚类1：前100个数:",list1[:100],'\n')
print("聚类2：前100个数:",list2[:100],'\n')
print("聚类2：前100个数:",list3[:100],'\n')
