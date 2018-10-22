import random 
import pandas as pd
import numpy as np
import tool

#设置精度小数点后两位
np.set_printoptions(precision=2)

#读取文件
df=pd.read_csv("waveform.data",header = None)

#增加20%的高斯噪声
for x in range(5000*22*0.2):
	i = random.randint(0,21)
	j = random.randint(0,4999)
	df[i][j] += random.gauss(0,0.5)  #均值维0，方差为0.5的高斯噪声


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
list_sum = []

result = 1

while result:
	list1.clear()
	list2.clear()
	list3.clear()
	result = tool.circle_o (df,cent1,cent2,cent3,list_sum,list1,list2,list3,result)
	

print("聚类1：前100个数:",list1[:100],'\n')
print("聚类2：前100个数:",list2[:100],'\n')
print("聚类2：前100个数:",list3[:100],'\n')
