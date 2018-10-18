import pandas as pd
import numpy as np

#循环计算各点距离质心的距离，并根据距离划分相应类
def circle (df,cent1,cent2,cent3,list1,list2,list3,result):
	for j in range(df.shape[0]):
		for i in range(df.shape[1]):
			a = np.abs(df[i][j]-cent1)
			b = np.abs(df[i][j]-cent2)
			c = np.abs(df[i][j]-cent3)

			if a<b and a<c:
				list1.append(df[i][j])
			if b<a and b<c:
				list2.append(df[i][j])
			if c<a and c<b:
				list3.append(df[i][j])
			if a==b and a==c:
				list1.append(df[i][j])

	nd1 = np.array(list1)
	nd2 = np.array(list2)
	nd3 = np.array(list3)

	cent_n1 = round(np.mean(nd1),2)
	cent_n2 = round(np.mean(nd2),2)
	cent_n3 = round(np.mean(nd3),2)

	if cent_n1 != cent1:
		cent1 = cent_n1
	if cent_n2 != cent2:
		cent2 = cent_n2
	if cent_n3 != cent3:
		cent3 = cent_n3

	if cent_n1 == cent1 and cent_n2 == cent2 and cent_n3 == cent3:
		result = 0
	else:
		result = 1

	return result




#循环计算图像各像素点距离质心的距离，并根据距离划分相应类
def pic (img,img_array,cent1,cent2,cent3,cent4,list1,list2,list3,list4,result):
	for i in range(img.size[0]):
		for j in range(img.size[1]):
			a = np.sum(np.square(np.array(img_array[i,j]) - np.array(cent1)))
			b = np.sum(np.square(np.array(img_array[i,j]) - np.array(cent2)))
			c = np.sum(np.square(np.array(img_array[i,j]) - np.array(cent3)))
			d = np.sum(np.square(np.array(img_array[i,j]) - np.array(cent4)))

			if a<b and a<c and a<d:
				list1.append(img_array[i,j])
			if b<a and b<c and b<d:
				list2.append(img_array[i,j])
			if c<a and c<b and c<d:
				list3.append(img_array[i,j])
			if d<a and d<b and d<c:
				list4.append(img_array[i,j])
			if a==b and a==c and a==d:
				list1.append(img_array[i,j])

	#思想，我需要求出各个R,N,G在列表中相同位置的平均值，
	#巧妙地想到了利用矩阵。首先将list转换为arry，之后进行转置，
	#就将每一列表相同位置的值转到了同一行，这样就可以带进函数求平均值
	nd1 = np.array(list1).T
	nd2 = np.array(list2).T
	nd3 = np.array(list3).T
	nd4 = np.array(list4).T

	cent_n1 = [ round(np.mean(nd1[0])), round(np.mean(nd1[1])), round(np.mean(nd1[2])) ]
	cent_n2 = [ round(np.mean(nd2[0])), round(np.mean(nd2[1])), round(np.mean(nd2[2])) ]
	cent_n3 = [ round(np.mean(nd3[0])), round(np.mean(nd3[1])), round(np.mean(nd3[2])) ]
	cent_n4 = [ round(np.mean(nd4[0])), round(np.mean(nd4[1])), round(np.mean(nd4[2])) ]

	if cent_n1 != cent1:
		cent1 = cent_n1
	if cent_n2 != cent2:
		cent2 = cent_n2
	if cent_n3 != cent3:
		cent3 = cent_n3
	if cent_n4 != cent4:
		cent4 = cent_n4

	if cent_n1 == cent1 and cent_n2 == cent2 and cent_n3 == cent3 and cent_n4 == cent4:
		result = 0
	else:
		result = 1

	return result

