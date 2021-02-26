import cv2
import timeit

# 영상 정보 불러오기
video = cv2.VideoCapture('KITTI.mp4')

while True:

    ret, frame = video.read()
    
    if ret is True:
        
        cv2.imshow('video',frame)   

        if cv2.waitKey(1) > 0 :  
            break