import cv2
import timeit

def image_LAB(img):  ## Using the LAB_Convert,correction image's Light
    lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
    l, a, b = cv2.split(lab)
    clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8, 8))
    cl = clahe.apply(l)
    limg = cv2.merge((cl, a, b))
    img = cv2.cvtColor(limg, cv2.COLOR_LAB2BGR)

def videocapture(cam,cascade):
	while True:
		start_t = timeit.default_timer()
		ret,img = cam.read()
		img = cv2.resize(img,dsize=None,fx=0.75,fy=0.75)
		image_LAB(img)
		gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

		results = cascade.detectMultiScale(gray,scaleFactor=1.5,minNeighbors=5,minSize=(20,20))

		for box in results:
			x,y,w,h = box
			cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,255),thickness=2)
		end_t = timeit.default_timer()
		FPS = 'fps'+str(int(1./(end_t-start_t)))
		cv2.putText(img,FPS,(30,30),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),1)
		cv2.imshow('face',img)
		if cv2.waitKey(1)>0:
			break

def imgDetector(img,cascade):
	img = cv2.resize(img,dsize=None,fx=0.75,fy=0.75)
	gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	results = cascade.detectMultiScale(gray,scaleFactor=1.5,minNeighbors=5,minSize=(20,20))

	for box in results:
		x,y,w,h = box
		cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,255),thickness=2)
	cv2.imshow('facenet',img)
	cv2.waitKey(10000)

cascade = 'haarcascade_frontalface_alt.xml'
cas = cv2.CascadeClassifier(cascade)

cam = cv2.VideoCapture('../media/video.mp4')
img = cv2.imread('../media/sample.jpg')
flag = input("if You Want to VideoDetect you input a 'V' \n you Want a ImageDetect, you input a I : " )
if flag == 'I' or flag == 'i':
	imgDetector(img,cas)
elif flag == 'V' or flag == 'v':
	videocapture(cam,cas)