import cv2
import numpy as np
import time

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
lines = cv2.HoughLinesP(edges,1,np.pi/180,50,minLineLength,maxLineGap)
lines2 = cv2.HoughLines(edges,1,np.pi/180,70)
#print(lines2)
img1 = img.copy()
img2 = img.copy()
img3 = img.copy()
img4 = img.copy()
j = 0
x1 = 580
x2 = 123
y1 = 123
y2 = 314
temp = []
k=0
f = 0
for key1,line2 in enumerate(lines2):
	j+=1
	a = np.cos(line2[0][1])
	b = np.sin(line2[0][1])
	#print("ab", line2[0][1] , line2[0][0] )
	#time.sleep(3)
	x0 = a*line2[0][0]
	y0 = b*line2[0][0]
	x1 = int(x0 + 1000*(-b))
	y1 = int(y0 + 1000*(a))
	x2 = int(x0 - 1000*(-b))
	y2 = int(y0 - 1000*(a))
	theta = line2[0][1]*90
	temp.append([line2[0][0],line2[0][1]])
	#for key,line in enumerate(lines2):
	#	if line2[0][0] != line[0][0] and line2[0][1] != line[0][1] and np.absolute(line2[0][0]-line[0][0])<=100 and np.absolute(line2[0][1]-line[0][1])<=0.1:
	#		del(lines2[key])
#print(temp)
#print(lines)
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
	for key,line1 in enumerate(temp):
		if line1[0] != line[0] and line1[1] != line[1] and np.absolute(line1[0]-line[0])<=160 and np.absolute(line1[1]-line[1])<=0.1:
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
	print("XY10 ",x10,y10)

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
	x1 = int(x0 + 1000*(-b))
	y1 = int(y0 + 1000*(a))
	x2 = int(x0 - 1000*(-b))
	y2 = int(y0 - 1000*(a))
	if x2-x1==0:
		x2+=1
	k=(y2-y1)/(x2-x1)*-1
	b=(x1*y2-x2*y1)/(x1-x2)
	ugol=np.arctan(k)*180/np.pi
	print("ugol ",ugol)
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
	if ugol>=20 and ugol<=60:
		cv2.line(img4,(x1,y1),(x2,y2),(255,0,0),2)
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
	if ugol>=-60 and ugol<=-20:
		cv2.line(img4,(x1,y1),(x2,y2),(0,255,0),2)
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
cv2.line(img4,(tempx1,tempy1),(tempx2,tempy2),(255,255,0),2)
cv2.line(img4,(tempx11,tempy11),(tempx22,tempy22),(255,0,255),2)

cv2.line(img4,(btempx1,btempy1),(btempx2,btempy2),(0,0,255),2)
cv2.line(img4,(btempx11,btempy11),(btempx22,btempy22),(0,0,200),2)
x3 = intersectionX(tempx1,tempx2,tempy1,tempy2,tempx11,tempx22,tempy11,tempy22)
y3 = intersectionY(tempx1,tempx2,tempy1,tempy2,tempx11,tempx22,tempy11,tempy22)

cv2.line(img4,(x3,y3),(x3,shape[1]),(255,255,255),2) # middle
cv2.line(img4,(ltempx1,ltempy1),(ltempx2,ltempy2),(0,0,0),2)
cv2.line(img4,(rtempx1,rtempy1),(rtempx2,rtempy2),(0,0,0),2)

cv2.imwrite('test_2_4.jpg',img4)
for line in temp:
	f+=1
	a = np.cos(line[1])
	b = np.sin(line[1])
	#print("ab", line2[0][1] , line2[0][0] )
	#time.sleep(3)
	x0 = a*line[0]
	y0 = b*line[0]
	print("XY",x0,y0)
	x1 = int(x0 + 1000*(-b))
	y1 = int(y0 + 1000*(a))
	x2 = int(x0 - 1000*(-b))
	y2 = int(y0 - 1000*(a))
	cv2.line(img1,(x1,y1),(x2,y2),(0,0,255),2)
cv2.imwrite('test_2.jpg',img1)
i=0


for line in lines:
	i+=1
	cv2.line(img,(line[0][0],line[0][1]),(line[0][2],line[0][3]),(0,255,0),2)
cv2.imwrite('test_1.jpg',img)
cv2.imwrite('test1.jpg',blur)
print("lines count: ",i)
print("lines2WOD count: ",j)
print("lines2WD count: ",f)
