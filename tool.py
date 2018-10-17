import pandas as pd
import numpy as np

def circle (df,cent1,cent2,cent3,list1,list2,list3,result):
#循环计算各点距离质心的距离，并根据距离划分相应类
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
