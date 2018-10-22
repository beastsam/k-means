import random 
import pandas as pd
import numpy as np
import tool

from PIL import Image

#图像大小为98*69
#print(im.size,im.format,im.mode) 显示图片信息

img = Image.open("dog.jpg","r")

#加高斯噪声
for x in range(300):
	i0 = random.randint(0,img.size[0]-1)     
	j0 = random.randint(0,img.size[1]-1)
	img.putpixel((i0,j0),(0,0,0))

img_array=img.load()

#随机选择四个中心点作为初始质心
#（62，44）（57，51）（83，55）（53，36）
i1 = random.randint(0,img.size[0]-1)     
j1 = random.randint(0,img.size[1]-1)   
cent1 = img_array[i1,j1]

i2 = random.randint(0,img.size[0]-1)     
j2 = random.randint(0,img.size[1]-1)   
cent2 = img_array[i2,j2]

i3 = random.randint(0,img.size[0]-1)     
j3 = random.randint(0,img.size[1]-1)   
cent3 = img_array[i3,j3]

i4 = random.randint(0,img.size[0]-1)     
j4 = random.randint(0,img.size[1]-1)   
cent4 = img_array[i4,j4]

print(i1,j1,"\n",i2,j2,"\n",i3,j3,"\n",i4,j4)

#聚类存储列表
list1 = []
list2 = []
list3 = []
list4 = []
list_sum = []

result = 1

while result:
	list1.clear
	list2.clear
	list3.clear
	list4.clear
	result = tool.pic_o (img,img_array,cent1,cent2,cent3,cent4,list_sum,list1,list2,list3,list4,result)
	
imgnew1 = Image.new("RGB",(img.size[0],img.size[1]))
imgnew2 = Image.new("RGB",(img.size[0],img.size[1]))
imgnew3 = Image.new("RGB",(img.size[0],img.size[1]))
imgnew4 = Image.new("RGB",(img.size[0],img.size[1]))

#三个参数依次为R,G,B,A   R：红 G:绿 B:蓝 A:透明度
#白色（225，255，255） 黑色（0，0，0）
pixTuple = (255,255,255)
for i in range(img.size[0]):
	for j in range(img.size[1]):
		if img_array[i,j] in list1:
			imgnew1.putpixel((i,j),img_array[i,j])
		else:
			imgnew1.putpixel((i,j),pixTuple)

		if img_array[i,j] in list2:
			imgnew2.putpixel((i,j),img_array[i,j])
		else:
			imgnew2.putpixel((i,j),pixTuple)

		if img_array[i,j] in list3:
			imgnew3.putpixel((i,j),img_array[i,j])
		else:
			imgnew3.putpixel((i,j),pixTuple)

		if img_array[i,j] in list4:
			imgnew4.putpixel((i,j),img_array[i,j])
		else:
			imgnew4.putpixel((i,j),pixTuple)

imgnew1.save('list1.jpg')
imgnew2.save('list2.jpg')
imgnew3.save('list3.jpg')
imgnew4.save('list4.jpg')

print("打印图片\n")




