import cv2
import os

for i in os.listdir():
	if i[-1] == "g":
		img = cv2.imread(i)
		img = cv2.resize(img,(700,500))
		cv2.imwrite("1"+i,img)
