import cv2
import numpy as np
import time
import main_test

def intersectionX(x1,x2,y1,y2,x3,x4,y3,y4):
	return int(((x1*y2-y1*x2)*(x3-x4)-(x1-x2)*(x3*y4-y3*x4))\
		/((x1-x2)*(y3-y4)-(y1-y2)*(x3-x4)))
def intersectionY(x1,x2,y1,y2,x3,x4,y3,y4):
	return int(((x1*y2-y1*x2)*(y3-y4)-(y1-y2)*(x3*y4-y3*x4))\
		/((x1-x2)*(y3-y4)-(y1-y2)*(x3-x4)))
img = cv2.imread('test.jpg')
shape = img.shape
blur = cv2.blur(img,(3,3))
gray = cv2.cvtColor(blur,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,200,300,apertureSize = 3)
cv2.imwrite('test_gray.jpg',edges)
minLineLength = 500
maxLineGap = 20


GoodAtLines=True
Thresh = 70
while (GoodAtLines):
	lines2 = cv2.HoughLines(edges,1,np.pi/180,Thresh)
	if len(lines2)>2000:
		Thresh+=10
	else:
		GoodAtLines = False

#print(lines2)
img1 = img.copy()
img2 = img.copy()
img3 = img.copy()
img4 = img.copy()
j = 0
temp = []
k=0
f = 0
for key1,line2 in enumerate(lines2):
	j+=1
	a = np.cos(line2[0][1])
	b = np.sin(line2[0][1])
	x0 = a*line2[0][0]
	y0 = b*line2[0][0]
	x1 = int(x0 + 1000*(-b))
	y1 = int(y0 + 1000*(a))
	x2 = int(x0 - 1000*(-b))
	y2 = int(y0 - 1000*(a))
	theta = line2[0][1]*90
	temp.append([line2[0][0],line2[0][1]])

for line in temp:
	a = np.cos(line[1])
	b = np.sin(line[1])
	x0 = a*line[0]
	y0 = b*line[0]
	x1 = int(x0 + 1000*(-b))
	y1 = int(y0 + 1000*(a))
	x2 = int(x0 - 1000*(-b))
	y2 = int(y0 - 1000*(a))
	cv2.line(img3,(x1,y1),(x2,y2),(0,0,255),2)
cv2.imwrite('test_2_3.jpg',img3)
for line in temp:
	for key,line1 in enumerate(temp): #line1 - line = bilo 160
		if line1[0] != line[0] and line1[1] != line[1] and np.absolute(line1[0]-line[0])<=50 and np.absolute(line1[1]-line[1])<=0.1:
			del(temp[key])

for line in temp:
	a = np.cos(line[1])
	b = np.sin(line[1])
	x0 = a*line[0]
	y0 = b*line[0]
	x1 = int(x0 + 1000*(-b))
	y1 = int(y0 + 1000*(a))
	x2 = int(x0 - 1000*(-b))
	y2 = int(y0 - 1000*(a))
	cv2.line(img2,(x1,y1),(x2,y2),(0,0,255),2)
cv2.imwrite('test_2_2.jpg',img2)

for line in temp:
	a1 = np.cos(line[1])
	b1 = np.sin(line[1])
	x10 = a1*line[0]
	y10 = b1*line[0]
	#print("XY10 ",x10,y10)

	for key,line1 in enumerate(temp):
		a = np.cos(line1[1])
		b = np.sin(line1[1])
		x0 = a*line1[0]
		y0 = b*line1[0]
		if  line1[0] != line[0] and np.absolute(x10-x0)<=20 and np.absolute(y10-y0)<=20:
			del(temp[key])
ktemp = 10000000
ktemp1 = 10000000
ktemp3 = -10000000
ktemp4 = -10000000
xMin = 10000
xMax = 0
for line in temp:
	a = np.cos(line[1])
	b = np.sin(line[1])
	x0 = a*line[0]
	y0 = b*line[0]
	x1 = int(x0 + 2000*(-b))
	y1 = int(y0 + 2000*(a))
	x2 = int(x0 - 2000*(-b))
	y2 = int(y0 - 2000*(a))
	if x2-x1==0:
		x2+=1
	k=(y2-y1)/(x2-x1)*-1
	b=(x1*y2-x2*y1)/(x1-x2)
	ugol=np.arctan(k)*180/np.pi
	"""
	if ugol>=80 and ugol<=100 or ugol>=-100 and ugol<=-80:
		if x1 < xMin:
			xMin = x1
			ltempx1 = x1
			ltempx2 = x2
			ltempy1 = y1
			ltempy2 = y2
		if x1 > xMax:
			xMax = x1
			rtempx1 = x1
			rtempx2 = x2
			rtempy1 = y1
			rtempy2 = y2
		#cv2.line(img4,(x1,y1),(x2,y2),(0,0,0),2)
	"""
	if ugol>=-6 and ugol<=60:
		#cv2.line(img4,(x1,y1),(x2,y2),(0,0,0),2)
		if b<ktemp:
			ktemp = b
			tempx1 = x1
			tempx2 = x2
			tempy1 = y1
			tempy2 = y2
		if b>ktemp3:
			ktemp3 = b
			btempx1 = x1
			btempx2 = x2
			btempy1 = y1
			btempy2 = y2
	if ugol>=-60 and ugol<=6:
		#cv2.line(img4,(x1,y1),(x2,y2),(0,255,0),2)
		if b<ktemp1:
			ktemp1 = b
			tempx11 = x1
			tempx22 = x2
			tempy11 = y1
			tempy22 = y2
		if b>ktemp4:
			ktemp4 = b
			btempx11 = x1
			btempx22 = x2
			btempy11 = y1
			btempy22 = y2
cv2.line(img4,(tempx1,tempy1),(tempx2,tempy2),(255,255,0),2) #TL
cv2.line(img4,(tempx11,tempy11),(tempx22,tempy22),(255,0,255),2) #TR

cv2.line(img4,(btempx1,btempy1),(btempx2,btempy2),(0,0,255),2) #BR
cv2.line(img4,(btempx11,btempy11),(btempx22,btempy22),(0,244,200),2) #BL

#if ltempx1>200:
#	ltempx1,ltempx2,ltempy1,ltempy2 = (0, 0, 0, shape[1])
ltempx1,ltempx2,ltempy1,ltempy2 = (0, 0, 0, shape[1])
rtempx1,rtempx2,rtempy1,rtempy2 = (shape[1], shape[1], 0, shape[0])


x2 = intersectionX(tempx1,tempx2,tempy1,tempy2,tempx11,tempx22,tempy11,tempy22)#MiddleTopPoint
y2 = intersectionY(tempx1,tempx2,tempy1,tempy2,tempx11,tempx22,tempy11,tempy22)

x1 = intersectionX(tempx1,tempx2,tempy1,tempy2,ltempx1,ltempx2,ltempy1,ltempy2)#TopLeftPoint
y1 = intersectionY(tempx1,tempx2,tempy1,tempy2,ltempx1,ltempx2,ltempy1,ltempy2)

x3 = intersectionX(btempx11,btempx22,btempy11,btempy22,x2,x2,y2,shape[1])#MiddleBottomPoint
y3 = intersectionY(btempx11,btempx22,btempy11,btempy22,x2,x2,y2,shape[1])

x4 = intersectionX(btempx11,btempx22,btempy11,btempy22,ltempx1,ltempx2,ltempy1,ltempy2)#BottomLeftPoint
y4 = intersectionY(btempx11,btempx22,btempy11,btempy22,ltempx1,ltempx2,ltempy1,ltempy2)
tempt = 'test_warp.jpg'
main_test.Transform(img,tempt, x1,y1,x2,y2,x3,y3,x4,y4)
cv2.line(img4,(x2,y2),(x2,shape[1]),(255,255,255),2) # middle
tempt = 'test_warp2.jpg'
x1, y1 = x2, y2
#print(tempx11,tempx22,tempy11,tempy22,rtempx1,rtempx2,rtempy1,rtempy2)
x2 = intersectionX(tempx11,tempx22,tempy11,tempy22,rtempx1,rtempx2,rtempy1,rtempy2)#TopRightPoint
y2 = intersectionY(tempx11,tempx22,tempy11,tempy22,rtempx1,rtempx2,rtempy1,rtempy2)

x3 = intersectionX(btempx1,btempx2,btempy1,btempy2,rtempx1,rtempx2,rtempy1,rtempy2)#BottomRightPoint
y3 = intersectionY(btempx1,btempx2,btempy1,btempy2,rtempx1,rtempx2,rtempy1,rtempy2)

x4 = intersectionX(btempx1,btempx2,btempy1,btempy2,x1,x1,y1,shape[1])#BottomLeftPoint
y4 = intersectionY(btempx1,btempx2,btempy1,btempy2,x1,x1,y1,shape[1])
#print(x1,y1,x2,y2,x3,y3,x4,y4)
main_test.Transform(img,tempt, x1,y1,x2,y2,x3,y3,x4,y4)
#cv2.line(img4,(ltempx1,ltempy1),(ltempx2,ltempy2),(0,20,0),2) #LeftVert
#cv2.line(img4,(rtempx1,rtempy1),(rtempx2,rtempy2),(0,0,0),2) # RightVert

cv2.imwrite('test_2_4.jpg',img4)
for line in temp:
	f+=1
	a = np.cos(line[1])
	b = np.sin(line[1])
	x0 = a*line[0]
	y0 = b*line[0]
	x1 = int(x0 + 1000*(-b))
	y1 = int(y0 + 1000*(a))
	x2 = int(x0 - 1000*(-b))
	y2 = int(y0 - 1000*(a))
	cv2.line(img1,(x1,y1),(x2,y2),(0,0,255),2)
cv2.imwrite('test_2.jpg',img1)
i=0

print("lines2WOD count: ",j)
print("lines2WD count: ",f)
#cv2.imwrite('test1.jpg',blur)
